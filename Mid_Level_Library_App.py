import os
kitapliste = list()

menu = """
1-Kitap ver
2-Kitap al
3-Kitapları Göster
Q-Çıkış
"""

def kitapver(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Verdiğiniz Kitap için Teşekkürler...")
    input("Ana menüye dönmek için enter'a basın")

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapal(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitap Alma İşlemi Başarılı")
        input("Ana menüye dönmek için enter'a basın")
    else:
        print("İstediğiniz Kitap Bulunamadı...")
        input("Ana menüye dönmek için enter'a basın")

def listele(liste):
    for a in liste:
        print("Kitap Adı :{} \nYazar :{}".format(a[0],a[1]))
    input("Ana menüye dönmek için enter'a basın")

while True:
    os.system("cls")
    print(menu)
    secim = input("İşlem numarası seçin:")

    if secim == "1":
        ad = input("Kitap Adı : ")
        yazar = input("Yazarı : ")
        kitap = (ad,yazar)
        kitapver(kitap,kitapliste)
    elif secim == "2":
        ad = input("Kitap Adı : ")
        yazar = input("Yazarı : ")
        kitap = (ad, yazar)
        kitapal(kitap,kitapliste)
    elif secim == "3":
        listele(kitapliste)
    elif secim == "Q" or secim == "q":
        quit()
    else:
        print("Hatalı Seçim, Ana Menüye Yönlendiriliyorsunuz ...")

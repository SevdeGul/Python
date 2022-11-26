kitapliste = list()

menu = """
1-Kitap Ekle
2-Kitapları Göster
Q-Çıkış
"""

def kitapekle(liste,kitap):
    liste += [kitap]
    print("Kitap Eklendi")
    input("Ana menüye dönmek için enter'a basınız...")

def listele(liste):
    for a in liste:
        print("Kitap Adı : {}".format(a))
    input("Ana menüye dönmek için enter'a basınız...")

def cikis():
    quit()

while True:
    print(menu)
    secim = input("Seçiminiz : ")

    if secim == "1":
        ad = input("Kitap Adı: ")
        kitapekle(kitapliste,ad)
    elif secim == "2":
        listele(kitapliste)
    elif secim == "Q" or secim == "q":
        cikis()
    else:
        print("Hatalı Seçim, Ana Menüye Yönlendiriliyorsunuz ...")

masalar = dict()
for a in range(20):
    masalar[a] = 0

def ekle():
    masano = int(input("Masa No : "))
    gecerli = masalar[masano]
    eklenecek = float(input("Eklenecek Ücret : "))
    toplam = gecerli + eklenecek
    masalar[masano] = toplam

def sil():
    masano = int(input("Masa No : "))
    gecerli = masalar[masano]
    silinecek = float(input("Silinecek Ücret : "))
    toplam = gecerli - silinecek
    if toplam < 0:
        input("İşlemde hata var, Ana menüye dönmek için enter'a basın...")
    else:
        masalar[masano] = toplam
        input("Ana menüye dönmek için enter'a basın...")

def kontrol(dosya):
    try:
        dosya = open(dosya)
        veri = dosya.read()
        veri = veri.split("\n")
        veri.pop()
        dosya.close()
        flag = True
    except FileNotFoundError:
        dosya = open(dosya,"w")
        dosya.close()
        print("Yeni dosya oluşturuldu")
        flag = False
    if flag:
        for a in enumerate(veri):
            masalar[a[0]]=float(a[1])
    else:
        pass

def guncelle():
    dosya = open("defter.txt","w")
    for a in range(20):
        ucret = masalar[a]
        ucret = str(ucret)
        dosya.write(ucret + "\n")
    dosya.close()

def ana():

    kontrol("defter.txt")

    while True:

        guncelle()

        print("""
        Lokanta Hesap Uygulamasına Hoş Geldiniz...
        
        1) Masaları Görüntüle
        2) Hesap Ekle
        3) Hesap Sil
        Q) Çıkış
        
        """)
        secim = input("İşlem numarası giriniz...")

        if secim == "1":
            for a in range(20):
                print("Masa {} için hesap: {}".format(a,masalar[a]))
            input("Ana menüye dönmek için enter'a basın...")

        elif secim == "2":
            ekle()
            input("Ana menüye dönmek için enter'a basın...")

        elif secim == "3":
            sil()

        elif secim == "Q" or secim == "q":
            quit()
        else:
            quit()

ana()

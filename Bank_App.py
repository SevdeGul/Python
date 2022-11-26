class Musteri():
    def __init__(self,TC,SIFRE,ISIM):
        self.tc = TC
        self.sifre = SIFRE
        self.isim = ISIM
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self,TC,SIFRE,ISIM):
        self.musteriler.append(Musteri(TC,SIFRE,ISIM))
        print("Bankamıza Kayıt Olduğunuz İçin Teşekkürler...")

banka = Banka()

while True:
    print("""
    1) Müşteriyim
    2) Müşteri Olmak İstiyorum
    
    """)
    secim = int(input("Seçiminiz : "))
    if secim == 1:
        for a in banka.musteriler:
            tcx = a.tc
            TC = input("TC : ")
            if TC in tcx:
                for musteri in banka.musteriler:
                    if TC == musteri.tc:
                        sifre = input("Şifre : ")
                        if sifre == musteri.sifre:
                            while True:
                                print("Hoş Geldiniz Sayın {}".format(musteri.isim))
                                print("""
                                        1) Bakiye Öğrenme
                                        2) Para Yatır (kendi hesabıma)
                                        3) Para Yatır (başka hesaba)
                                        4) Para Çek
                                        Q) Çıkış
                        
                                        """)
                                secim2 = input("Seçiminiz : ")
                                if secim2 == "1":
                                    print("Bakiyeniz : {}".format(musteri.bakiye))
                                    input("Ana menüye dönmek için enter'a basın...")
                                elif secim2 == "2":
                                    miktar = int(input("Miktar : "))
                                    onay = input("Kendi hesabınıza {} TL para yatıırılacak onaylıyor musunuz? (Y/N)".format(miktar))
                                    if onay == "Y" or onay == "y":
                                        musteri.bakiye += miktar
                                        print("İşlem Başarılı")
                                        input("Ana menüye dönmek için enter'a basın...")
                                    elif onay == "N" or onay == "n":
                                        print("İşlem Başarısız")
                                        input("Ana menüye dönmek için enter'a basın...")
                                    else:
                                        print("Hatalı giriş, İşlem İptal Edidi")
                                        input("Ana menüye dönmek için enter'a basın...")
                                elif secim2 == "3":
                                    arananTC = input("Müşteri TC : ")
                                    if arananTC in tcx:
                                        for digermusteri in banka.musteriler:
                                            if arananTC == digermusteri.tc:
                                                miktar = int(input("Miktar : "))
                                                if miktar <= musteri.bakiye:
                                                    onay = input("{} adlı müşterimizin hesabına {} TL para yatıırılacak onaylıyor musunuz? (Y/N)".format(digermusteri.isim,miktar))
                                                    if onay == "Y" or onay == "y":
                                                        digermusteri.bakiye += miktar
                                                        musteri.bakiye -= miktar
                                                        print("İşlem Başarılı")
                                                        input("Ana menüye dönmek için enter'a basın...")
                                                    elif onay == "N" or onay == "n":
                                                        print("İşlem Başarısız")
                                                        input("Ana menüye dönmek için enter'a basın...")
                                                    else:
                                                        print("Hatalı giriş, İşlem İptal Edidi")
                                                        input("Ana menüye dönmek için enter'a basın...")
                                                else:
                                                    print("Bakiyeniz Yetersiz")
                                                    input("Ana menüye dönmek için enter'a basın...")
                                            else:
                                                print("Müşteri Bulunamadı")
                                                input("Ana menüye dönmek için enter'a basın...")
                                    else:
                                        print("Müşteri Bulunamadı")
                                        input("Ana menüye dönmek için enter'a basın...")
                                elif secim2 == "4":
                                    miktar = int(input("Miktar : "))
                                    if miktar <= musteri.bakiye:
                                        musteri.bakiye -= miktar
                                        print("İşlem Başarılı")
                                    else:
                                        print("Bakiyeniz Yetersiz")
                                        input("Ana menüye dönmek için enter'a basın...")
                                elif secim2 == "Q" or secim2 == "q":
                                    break
                                else:
                                    print("Hatalı Seçim")
                                    input("Ana menüye dönmek için enter'a basın...")
                        else:
                            print("Hatalı Seçim")
                            input("Ana menüye dönmek için enter'a basın...")
                    else:
                        print("Hatalı Seçim")
                        input("Ana menüye dönmek için enter'a basın...")
            else:
                print("Hatalı Seçim")
                input("Ana menüye dönmek için enter'a basın...")
    elif secim == 2:
        tc__ = input("TC : ")
        isim__ = input("İSİM : ")
        sifre__ = input("ŞİFRE : ")
        banka.musteri_ol(tc__,sifre__,isim__)
        input("Ana menüye dönmek için enter'a basın...")
    else:
        print("Hatalı Seçim")
        input("Ana menüye dönmek için enter'a basın...")




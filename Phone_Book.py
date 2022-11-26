while True:
    rehber = {
        "kisi1": {
            "cep":"5425425424",
            "ev":"5385385383",
            "is":"5375375373"
        },

        "kisi2":{
            "cep":"5365365363",
            "ev": "5395395393",
            "is":"5355355353"
        }

    }
    isimler = rehber.keys()
    kisi = input("Kişi Adı : ")
    tel = input("Telefon Numarası : ")

    if kisi in isimler:
        flag = True
    else:
        flag = False

    if flag:
        print(rehber.get(kisi).get(tel,"numara bulunamadı"))
    else:
        print("aradığınız kişi bulunamadı")
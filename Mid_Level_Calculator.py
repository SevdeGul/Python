a = float(input("İlk Sayıyı Giriniz: "))
c = input("Yapmak istediğiniz İşlemi Seçiniz: (+,-,*,/,**)")
b = float(input("İkinci Sayıyı Giriniz: "))

if(c == "+"):
    d = a + b
    print("Sonuç :",d)
elif(c == "-"):
    d = a - b
    print("Sonuç :",d)
elif(c == "*"):
    d = a * b
    print("Sonuç :",d)
elif(c == "/"):
    d = a / b
    print("Sonuç :",d)
elif(c == "**"):
    d = a ** b
    print("Sonuç :",d)
else:
    print("Geçersiz İşlem...")

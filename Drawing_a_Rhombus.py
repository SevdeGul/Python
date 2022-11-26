def sag(adet):
    for a in range(int(adet)):
        print("/",end="")

def sol(adet):
    for a in range(int(adet)):
        print("\\",end="")

def bosluk(adet):
    for a in range(int(adet)):
        print(" ",end="")

def atla(adet):
    for a in range(int(adet)):
        print()

def ust(cap):
    baslangic = (cap/2)-1
    for a in range(int(cap/2)):
        bosluk(baslangic-a)
        sag(1)
        bosluk(a*2)
        sol(1)
        atla(1)

def alt(cap):
    baslangic = cap-2
    for a in range(int(cap/2)):
        bosluk(a)
        sol(1)
        bosluk(baslangic-a*2)
        sag(1)
        atla(1)

def sekil(cap):
    ust(cap)
    alt(cap)

sekil(10)

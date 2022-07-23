import random

a = random.randrange(1,10)
h = []
print("Men 1 dan 10 gacha bir son o'yladim topa olasizmi \n")
while True:
    b = int(input("Taxminigizni kiritib ko'ring: "))
    h.append(b)
    if b == a:
        print("Ofarin siz to'g'ri topdingiz")
        break
    else:
        print("Afsus topa olmadingiz \n Yana bir bor urinib ko'ring \n")
        continue
print("Endi siz 1 dan 10 gacha bo'lgan son o'ylang men topaman")
g = []
while True:
    c = random.randrange(1,10)
    print(f"Siz o'ylagan son {c}")
    d = input("To'g'rimi?  Ha/Yuq ").lower()
    g.append(d)
    if d == "ha":
        print("Topdim")
        if len(h) > len(g):
            print("Afsus siz yutqazdingiz")
        elif len(h) < len(g):
            print("Tabriklayman siz yutdingiz")
        break
    elif d == "yuq":
        print("Afsus topa olmadim")
        continue
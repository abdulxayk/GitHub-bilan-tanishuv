en_uz = {"Apple":"Olma","Apricot":"O'rik","Peach":"Shaftoli","Cherry":"Olcha","Granate":"Anor","Strawberry":"Qulubnay",}
for son in range(1,100000):
    print(en_uz.get(input("So'z kiriting: ").title(),"Bnday kalit so'z yuq"))
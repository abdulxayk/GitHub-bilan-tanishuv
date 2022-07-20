
en_uz = {"Apple":"Olma","Apricot":"O'rik","Peach":"Shaftoli","Cherry":"Olcha","Granate":"Anor","Strawberry":"Qulubnay"}

for i in range(1,100000):
    a = input("do you want to proceed")
    if a=="yes" :
         print(en_uz.get(input("So'z kiriting: ").title(),"Bnday kalit so'z yuq"))
    else:
        break
    

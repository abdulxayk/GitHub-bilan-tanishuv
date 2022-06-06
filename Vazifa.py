davlatlar = {"AQSH":"Vashington","ROSSIYA":"Moskva","XITOY":"Pekin","YAPONIYA":"Tokio"}
for a in range(1,100):
    davlat = input("Davlat nomini kiriting: ").upper()
    if davlat in davlatlar.keys():
        print(davlatlar[davlat])
    elif davlat == 'AQSH' or davlat == 'AMERIKA QO\'SHMA SHTATLARI':
        print(davlatlar['AQSH'])
    elif davlat == "ROSSIYA" or davlat == "RASSIYA":
        print(davlatlar['ROSSIYA'])
    else:
        print(davlatlar.get(davlat,"Bunday malumot yuq"))

#en_uz = {"Apple":"Olma","Apricot":"O'rik","Peach":"Shaftoli","Cherry":"Olcha","Granate":"Anor","Strawberry":"Qulubnay",}
#for son in range(1,100000):
#    print(en_uz.get(input("So'z kiriting: ").title(),"Bnday kalit so'z yuq"))
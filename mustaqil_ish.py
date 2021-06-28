#ismlar = ['bekzod', 'sherzod', 'nodirbek']
narxi = float(input("Maxsulot narxini kirit: "))
olchami = float(input("Maxsulot o'lchamini kirit: "))
kopaytma = narxi * olchami
hisob = "Ikkala o'zgaruvchi ko'paytmasi {0} * {1} = {2}"
print(hisob.format(narxi, olchami, kopaytma))

def new_func():
    # Ism familiyalar kiritilsa Bekzod Eliboyev bo'lsa teskari chop etsin.
    ism = str(input("Ismni kiriting: "))
    fam = str(input("Familiyani kiriting: "))
    list_obratniy = ("{0} {1}")
    print(list_obratniy.format(fam.upper(), ism.upper()))
new_func()

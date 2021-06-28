"""x = "Salom"
print(type(x),x)

def myfunc():
    ozgaruvchi = ["birinchi", "ikkinchi", "uchunchi"]
    x, y, z = ozgaruvchi
    print(x,y,z)
myfunc()

def myfunc2():
#    x = "Bekzod"
    global x
    y = " Eliboyev"
    z = x + y
    print(type(z),z)
myfunc2()

def data_types():
    x = 1j
    x1 = ["olma", "anor"]
    x2 = ("olma", "anor")
    x3 = {"ism" : "Edik", "bo'yi" : "176"}
    print(type(x),x)
    print(type(x1),x1)
    print(type(x2),x2)
    print(type(x3),x3)

data_types()
"""
'''
def convert():
    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex

#convert from int to float:
    a = float(x)

#convert from float to int:
    b = int(y)

#convert from int to complex:
    c = complex(x)

    print(a)
    print(b)
    print(c)

    print(type(a),a)
    print(type(b),b)
    print(type(c),c)
convert()
import random
print(random.randrange(1, 1000))
'''
a = " Bekzodjon "     #O'zgaruvchi nomi
print(a.strip())    # Oraliq bo'sh joylarni olib tashlab chop etadi
def matrix():       #funksiya nomi
    global a        #Funksiya ichida global o'zgaruvchini hisobga olish
    print(a[:])     #Bu yerda matritsadan 0 dan boshlab ko'rsatilgan index gacha oladi (- pozitsiya o'ng tarafdan boshlanadi)
matrix()            #Bu siklni yopilishi

def sikl():         
    global a
    for x in a:     # Sikl boshlanishi
        print(x)    # matritsani elementlarini bittalab oladi sikl tugagunicha
sikl()

print("Bu so'zdagi simvollar soni",len(a[1:-1]), "ta")

def tanlash():
    global a
    if  "Bek" in a:
        print("Ha Bek so'zi mavjud !")
        if "Sher" not in a:
            print("Sher so'zi yo'q")
tanlash()

def upper_lower():
    global a
    print(a.upper()[:-4])
    print(a.lower()[:-4])
upper_lower()

def replace():
    global a
    print(a.replace("B", "Sh"))
#    print(a.replace("k","r"))
replace()
print("Bekzod")
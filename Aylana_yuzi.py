from math import pi
r = float(input("Aylana radiusini kiriting: "))
S = float(pi * r**2)
L = float(pi * 2 * r)
x = float(pi)
print(format(str(x) + " - Pi ning qiymati"))
print(format("Agar aylana radiusi " + str(r) + " sm bo'lsa \nUning yuzasi: " + str(S) + " sm ga teng!" + "\nAylana uzunligi: " + str(L)))


'''
aylana yuzasi va uzunligini topish

'''

def PI_qiymati():
    global L
    global r
    a = L / (2 * r)
    print("Pi ning qiymati: " + str(a))
PI_qiymati()

def togri_t_y_h():
    a = float(input("To'g'ri to'rtburchak A tomoni kiriting: "))
    b = float(input("To'g'ri to'rtburchak B tomoni kiriting: "))
    S = float(a * b)
    print(format(str(S) + " Yuza"))
togri_t_y_h()
print("Xush kelibsiz!!!")
def my_func():
    global L
    global r
    print("Nima qilish kerak" + str(L/r))
my_func()
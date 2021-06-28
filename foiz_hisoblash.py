'''
i1 = str(input("Birinchi so'z: "))
i2 = str(input("Ikkinchi so'z: "))
rep = ("{0}, {1}")
print(rep.format(i1.upper(), i2.upper()))
'''
def proc():
    x = float(input("Qiymatni kirit: "))
    y = float(input("Foizni kirit: "))
    z = float((x * y) / 100)
    print(str(x) + " ning\t" + str(y) + " foizi,\t" + str(z) + " ga teng!")
proc()
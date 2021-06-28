yosh = 27
ism = "Bekzod"
borgan = bool(True)

txt = "Mening ismim {0}, Yoshim {1} da, xizmatga {2}"

print(txt.format(ism, yosh, borgan) + " borgan")
#print(txt.casefold())

def zfill():
    tekst = "Bekzod"
    x = tekst.zfill(10)
    print(x)
zfill()

def find():
    a = "Salom mening dunyoyimga xush kelibsan."
   # x = a.find("k")    # Qatordan x ning qiymati berilgan simvol, so'z indeksini aniqlash
    x = a.index("k")    
    print(x)

find()

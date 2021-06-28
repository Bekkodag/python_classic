'''
raqamlar = input("Raqamlarni kiriting: ")
royhat = raqamlar.split(".")
yigma = tuple(royhat)
print("Ro'yhat : ", royhat)
print(type(royhat),"Yig'ma: ", yigma)
'''
filename = input("Fayl nomini kiriting: ")
qisqartma = filename.split(".")
print("Chiqish: " + repr(qisqartma[-1]))
# import random
# x = random.random()
# print(x)

from random import random
num = int(input("Masukkan Bilangan N : "))
for i in range(num):
    x = random()
    print("Perulangan Ke: {0} => {1}".format(i, x))
print("Selesai")


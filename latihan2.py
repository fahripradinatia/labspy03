
# list = []
# total = 0
# n = int(input("Masukkan nilai: "))
# for x in range(n):
#     nilai = int(input("Masukkan nilai ke-{} : ".format(x+1)))
#     array.append(nilai)
# print("Hasil nilai total adalah : {}".format(max(list)))

terbesar = []
while True:
    n = int(input("Masukkan Bilangan N: "))
    terbesar.append(n)
    if n == 0:
        break
print("Nilai Terbesar adalah : {}".format(max(terbesar)))





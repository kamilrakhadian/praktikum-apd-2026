# batas = 5
# for i in range(67):
#     print("Perulangan ke-", i)

# nilai = [75, 60, 80, 60, 50]
# for item in nilai:
#     if item > 70:
#         print(item, "Lulus")
#     else: 
#         print(item, "Tidak Lulus")

# for i in range(0, 11, 4): #range(start, stop, step)
#     print(i)

#nested for 
# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi

#while
# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")

#Kontrol perulangan break
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

#Kontrol perulangan continue
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
#continue lebih ke skip setelahnya jika kondisinya terpenuhi

# for i in range(10):
#     if i == 0:
#         continue
#     elif i == 5:
#         break
#     else:
#         print(i)

# for i in range(5):
#     print(i, end=", ")
#Gunakan end agar hasil output menyamping, jika tidak program akan membaca untuk print ke bawah

#studi kasus 1 modul 4
# n = int(input("nilai: "))
# jumlah_ganjil = 0
# for i in range(n):
#     if i % 2 == 0:
#         jumlah_ganjil += 1
#         print (i)
# print(f'jumlah_ganjil dalam {n}adalah : {jumlah_ganjil}')

#studi kasus 2 modul 4
# saldo = int(input("Masukkan jumlah saldo: "))
# while True:
#     expense = int(input("Masukkan jumlah pengeluaran: "))
#     saldo = saldo - expense
#     print(f'Sisa saldo anda: {saldo}')
#     if saldo > 0:
#         continue
#     if saldo < 0:
#         print("Saldo anda tidak mencukupi")
#         break

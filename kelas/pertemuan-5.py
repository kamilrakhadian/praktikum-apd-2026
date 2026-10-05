# aku1 = "kamil"
# aku2 = "rakha"
# aku3 = "akmil"
# print("1")
# print(aku1, aku2, aku3)
# print()

# print("2")
# listaku = ["kamil", "rakha", "akmil"]
# print(listaku)

# print("3")
# print(listaku[0],
#       listaku[1],
#       listaku[2])

# print("4")
# print(listaku[1])
# print(listaku[2])

# print("5")
# print(listaku[-1])
# print(listaku[-3])

#display list
# listaku = ["kamil", "rakha", "akmil"]
# print(listaku[:2])  #start:stop:step, pada baris kode ini start = 0, stop = 2, step = 1 (langsung stop sebelum index 2)
# for i in(listaku):
#     print(i)
# print()

# #update
# listaku.append("kaka")
# print(listaku)

# #update
# listaku.extend(["tampan", "sigma"]) #untuk memasukkan beberapa data sekaligus ke dalam list (langsung banyak)
# print(listaku)

# #update
# listaku.insert(1, "ganteng") #untuk memasukkan data ke dalam list pada index tertentu/nyisipin (index keberapa, elemen yang dimasukkan)
# print(listaku)

# #edit/mengubah elemen
# listaku[:2] = ["orang putih"]
# print(listaku)

# listaku[0:2] = ["orang hitam", "orang sawo", "orang kuning"] #mengubah beberapa elemen sekaligus
# print(listaku)

# #delete
# del listaku[2] #menghapus elemen pada index tertentu
# print(listaku)
# print(listaku[2])

# listaku.remove("orang sawo") #menghapus elemen tertentu
# print(listaku)

# del listaku[0:3] #menghapus beberapa elemen sekaligus
# print(listaku)

# #hapus dan menampilkan elemen yang dihapus
# ambilaku = listaku.pop(0)
# print(listaku) 
# print(ambilaku) #menampilkan elemen yang dihapus dengan pop
# print()

# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(angka[1:9:2]) #start:stop:step, pada baris kode ini start = 1, stop = 9, step = 2 (langsung stop sebelum index 9)
# print()

# angka0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# angka1 = [11, 12, 13]
# angka3 = angka0 * 3 #menggabungkan list
# print(angka3)

# #nested list
# line_up = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1]) # Output: Verstappen

# for i in line_up:
#     for j in i:
#         print(j)

# kamu = ["w", "d", "a", "p"]
# print(kamu)
# hapus = input("Masukkan huruf yang ingin dihapus: ")
# kamu.remove(hapus)
# print(kamu)
# print()

# kamu = ["w", "d", "a", "p"]
# print(kamu)
# hapus = int(input("Masukkan indeks huruf yang ingin dihapus: "))
# del kamu[hapus]
# print(kamu)

#tuple
# buah = ("jeruk", "mangga", "nanas", "semangka")
# print(buah)
# print()

# listbuah = list(buah) #mengubah tuple menjadi list
# listbuah.append("pisang") #menambahkan elemen ke dalam list
# buah = tuple(listbuah) #mengubah list menjadi tuple
# print(buah)

#metode seperti del remove pop extend insert bisa digunakan pada tuple jika diubah menjadi list terlebih dahulu, karena tuple bersifat immutable (tidak bisa diubah)

#unpack tuple
favgweh = ("roblos", "ml")
(letsgo, hmmz) = favgweh #unpacking tuple
print(hmmz)
print(letsgo)



#slicing akan sering digunakan pada posttest
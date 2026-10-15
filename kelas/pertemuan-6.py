# kartu = ["merah", "merah", "biru", "hijau"]
# print(kartu)

# set_baru = set(kartu)
# print(set_baru)

# kartu = ["merah", "merah", "biru", "hijau"]
# print(len(kartu))

# set_baru = set(kartu)
# print(len(set_baru))

# kartu = {"merah", "merah", "biru", "hijau"}
# for i in kartu:
#     print (i)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print (angka)

# kartu = {"merah", "merah", "biru", "hijau"}
# kartu.add("kuning")

# for i in kartu:
#     print (i)

# kartu = {"merah", "merah", "biru", "hijau"}
# kartu.remove("kuning")
# #jika elemen tiddak ditemukan maka akan error
# for i in kartu:
#     print (i)

# kartu = {"merah", "merah", "biru", "hijau"}
# kartu.discard("kuning")
# #jika elemen tiddak ditemukan tidak akan error
# for i in kartu:
#     print (i)

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)

#dictionary
# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }

# print(Biodata["NIM"])
# print(Biodata["KRS"][1])

# print(f"Nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))
#menggunakan get tidak akan menghasilkan error

# print(f"Nama saya adalah {Biodata['Nama']}")
# print(Biodata["Nama"])
# print(Biodata["Alamat"])
# print(Biodata["Alamat", "Key untuk alamat tidak ada"])

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }

# for i in game:
#     print(i)

# for i in game.keys():
#     print(i)
# #menambahkan .keys agar memperjelas apa yyang ingin ditampiljan

# for i in game.values():
#     print(i)
#menambahkan .values untuk menampilkan value dari key dalam dictionary

# for i, j in game.items():
#     print(f"{i} adalah jenis game {j}")
#atau cara yg dibawah ini
# for keys, values in game.items():
#     print(f"{keys} adalah jenis game {values}")

# game["resident evil"] = "horror"
# print(game)
# #menambahkn langsung ke dictionary

# #langsung menambahkan beberapa
# game.update({"resident evil" : "horror"
#              "Lecep : kotakpasir"})
# print(game)
# #atau menggunakan koma ,
# game.update({"resident evil" : "horror", "Lecep : kotakpasir"})
# print(game)

# tambah = game.setdefault("resident evil", "horror")
# print(game)
# print("Tipe game", game.setdefault("grow a garden", "gardening"))

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# del aset["luas"]
# print(aset)
# print(aset.get("luas"))

# print(aset)
# cache = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(cache)

# print(aset)
# aset.clear()
# print(aset)
#menghapus semua nilai/isi dictionary

# print("Panjang dictionary :", len(aset))
# print(len(aset))
#panjang dictionary menggunakan len

# menu = {
# "ayam geprek" : 15000,
# "ayam goreng" : 13000,
# "ayam bakar" : 17000,
# "nasi goreng" : 12000,
# "mie goreng" : 10000
# }
# menu_baru = menu.copy()
# menu_baru["nasi goreng"] = 15000
# print(menu)
# print(menu_baru)
#membuat variabel baru dari salinan menu

#membuat dictionary lanhsung mengguankan key
# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000
# menu = dict.fromkeys(key, value)
# print(menu)
#key langsung menyesuaikan dengan value, tidak bisa diotak atik

# menu = {
# "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
# "nasi" : ["nasi goreng", "nasi uduk"],
# "mie" : ["mie goreng rendang", "mie goreng aceh"],
# "kuah" : ["soto", "rawon", "sop iga"]
# }
# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
#     for kategori in j:
#         print(kategori)
#     print("")

#nested dictionary digunakan untuk menyimpan beberapa data akun user login
# data_siswa ={
#     "siswa1" :{
#     "nama" : "johan",
#     "kelas" : "a2",
#     "nilai" : "95"
#     },
#     "siswa2" :{
#         "nama" : "kamil",
#         "kelas" : "a2",
#         "nilai" : "100",
#     }
# }
# print(data_siswa["siswa1"]["nama"])
# print(data_siswa["siswa2"]["nama"])

# poli_umum = {"Andi", "Budi", "Citra", "Doni"}
# poli_gigi = {"Citra", "Doni", "Eka", "Fani"}
# seluruh_pasien = poli_umum.union(poli_gigi)
# print(seluruh_pasien)

set.data_user = {}
print("Silahkan Registrasi")
username_baru = input("Buat username: ")
nama_baru = input("Masukkan nama: ")
password_baru = input("Masukkan password: ")

set.data_user[username_baru] = {
    "Nama": nama_baru,
    "Password": password_baru,
    "Saldo" : 0,
    "Status" : "Nasabah"
}
print("Anda berhasil registrasi, silahkan login")
print(set.data_user)

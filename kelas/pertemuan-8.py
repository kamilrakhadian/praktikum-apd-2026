#built-in function & python library
#enumerate() – Memberi indeks pada iterable / bakalan sering digunakan untuk membaca data terutama pada PA
#import didahulukan/paling atas pada baris kode

# from prettytable import PrettyTable
# # Membuat objek tabel dan menentukan nama-nama kolom
# tabel = PrettyTable()
# tabel.field_names = ["NIM", "Nama Mahasiswa", "Prodi"]
# # Menambahkan satu baris data ke dalam tabel
# tabel.add_row(["2609106001", "Andi Alarice", "Informatika"])
# # Menambahkan beberapa baris data sekaligus menggunakan list di dalam list
# tabel.add_rows([
# ["2609106002", "Hammam Nopal", "Informatika"],
# ["2609106003", "Abimar LLM", "Sistem Informasi"]
# ])
#untuk menginput
# tabel.add_row([input("Nim"), input("nama"), input("prodi")])
# # Mengatur perataan teks pada kolom tertentu ('l' = kiri, 'c' = tengah, 'r'= kanan)
# tabel.align["Nama Mahasiswa"] = "l"
# print(tabel)

import inquirer
# Menyusun daftar pertanyaan menu
pertanyaan = [
    inquirer.List(
    "menu",
    message="Pilih menu aplikasi",
    choices=["Tambah Data", "Lihat Data", "Keluar"],
    ),
]
# Menampilkan prompt di terminal dan menyimpan hasil pilihan
jawaban = inquirer.prompt(pertanyaan)
print(jawaban) # Output berupa Dictionary, misal: {'menu': 'Tambah Data'}
print(jawaban["menu"]) # Mengambil nilai berdasarkan key 'menu': Tambah Data

#coba cari tahuq
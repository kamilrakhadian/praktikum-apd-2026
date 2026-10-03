user = "KAMIL"
passw = "025"

print("Selamat datang di program pendataan nilai siswa")
print("Silahkan masukkan data diri anda terlebih dahulu")
for i in range(3):
    username = str(input("Nama Pengguna: ")).upper()
    password = str(input("Masukkan 3 Digit Terakhir NIM: "))
    if username == user and password == passw:
        print()
        print("Akses diberikan")
        break
    elif username == user or password == passw:
        print("Format identitas salah, coba lagi")
    else:
        print("Identitas tidak dikenali, coba lagi")
else:
    print("Percobaan login telah habis!")
    print("Akses ditolak")
    exit()

data_siswa = []
while True:
    nama_siswa = str(input("Nama Siswa: "))
    kelas = str(input("Kelas: ")).upper()
    status_ujian = str(input("Apakah siswa ikut ujian? (Y/N) ")).upper()
    if status_ujian == "Y":
        jumlah_benar = int(input("Jumlah jawaban benar: "))
        jumlah_salah = int(input("Jumlah jawaban salah: "))
        total_nilai = jumlah_benar * 5
        nilai = total_nilai
    else:
        nilai = 0
    if nilai >= 80:
        kategori_nilai = "Sangat Baik"
    elif nilai >= 60:
        kategori_nilai = "Baik"
    elif nilai >= 40:
        kategori_nilai = "Cukup"
    else:
        kategori_nilai = "Perlu Belajar Lagi"

    data_siswa.append([
        nama_siswa, 
        kelas, 
        status_ujian, 
        nilai, 
        kategori_nilai
    ])
    jawab = input("Tambah data siswa? (Y/N) ").upper()
    if jawab == "N":
        break

kelas = []
for siswa in data_siswa:
    if siswa[1] not in kelas:
        kelas.append(siswa[1])
for i in kelas:
    print(f"========= Kelas {i} =========")
    for j in data_siswa:
        if j[1] == i:
            print("Nama Siswa     : ", j[0])
            print("Status Ujian   : ", j[2])
            print("Nilai          : ", j[3])
            print("Kategori Nilai : ", j[4])
            print()
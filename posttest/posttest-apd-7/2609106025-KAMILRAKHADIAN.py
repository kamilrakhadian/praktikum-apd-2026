
def menu_utama():
    os.system("cls")
    print("=SELAMAT DATANG=")
    print("===MENU UTAMA===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    opsi = input("Masukkan opsi (1-3): ")
    while opsi not in ("1", "2", "3"):
        print("Opsi keliru. Masukkan angka menu 1-3")
        opsi = input("Masukkan opsi (1-3): ")
    if opsi == "1":
        opsi1()
        jeda()
    elif opsi == "2":
        opsi2()
        jeda()
    elif opsi == "3":
        opsi3()

def opsi1():
    global pengguna
    os.system("cls")
    print("==Silahkan Login==")
    if pengguna == None:
        username = input("Masukkan username anda: ")
        if username in data_user:
            success = False
            while not success:
                password_nasabah = input("Masukkan password anda: ")
                if password_nasabah == data_user[username]["Password"]:
                    success = True
                    os.system("cls")
                    print("Login berhasil")
                    print("Selamat datang,", data_user[username]["Nama"])
                    if success:
                        pengguna = username
                        while pengguna != None:
                            if data_user[username]["Status"] == "Admin":
                                menu_admin()
                            else:
                                menu_nasabah()
                else:
                    print("Password salah, coba lagi")
def opsi2():
    os.system("cls")
    print("==Silahkan Registrasi==")
    username_baru = input("Buat username: ").strip()
    while username_baru in data_user:
        os.system("cls")
        print("Username telah digunakan, coba yang lain")
        username_baru = input("Buat username: ").strip()
    
    nama_baru = input("Masukkan nama: ").strip()
    password_baru = input("Masukkan password: ").strip()

    data_user[username_baru] = {
        "Nama": nama_baru,
        "Password": password_baru,
        "Saldo" : 0,
        "Status" : "Nasabah",
        "Riwayat Transaksi" : []
    }
    print("Anda berhasil registrasi, silahkan login")

def opsi3():
    global program
    if leave():
        program = False

def input_konfirmasi(feedback):
    while True:
        jawaban = input(feedback).strip().lower()
        if jawaban in ("y", "n"):
            return jawaban
        print("Opsi keliru. Masukkan y atau n.")

def leave():
    leave_system = input_konfirmasi("Keluar dari sistem (y/n)? : ")
    if leave_system == "y":
        print("Anda telah keluar dari sistem")
        print("Terimakasih telah menggunakan BANK SIGAM")
        return True
    return False

def leave_akun():
    global pengguna
    leave_account = input_konfirmasi("Keluar dari akun (y/n)? : ")
    if leave_account == "y":
        print("Anda telah log out.")
        pengguna = None
        return True
    return False

def jeda():
    input("\nTEKAN ENTER UNTUK MELANJUTKAN")

def menu_admin():
    os.system("cls")
    print("===MENU ADMIN===")
    print("1. Kelola Sampah")
    print("2. Kelola Data Nasabah")
    print("3. Exit akun")
    opsi_admin = input("Masukkan opsi (1-3): ")
    while opsi_admin not in ("1", "2", "3"):
        print("Opsi keliru. Masukkan angka menu 1-3")
        opsi_admin = input("Masukkan opsi (1-3): ")
    if opsi_admin == "1":
        opsiA1()
    elif opsi_admin == "2":
        opsiA2()
    elif opsi_admin == "3":
        leave_akun()

def opsiA1():
    os.system("cls")
    print("===MENU KELOLA SAMPAH===")
    print("1. Daftar Sampah")
    print("2. Tambah Jenis dan Harga Sampah")
    print("3. Update Harga Sampah")
    print("4. Hapus Sampah")
    print("5. Exit akun")
    opsi_kelola_sampah = input("Masukkan opsi (1-5): ")
    while opsi_kelola_sampah not in ("1", "2", "3", "4", "5"):
        print("Opsi keliru. Masukkan angka menu 1-5")
        opsi_kelola_sampah = input("Masukkan opsi (1-5): ")
    if opsi_kelola_sampah =="1":
        read_sampah()
        jeda()
    elif opsi_kelola_sampah =="2":
        create_sampah()
        jeda()
    elif opsi_kelola_sampah =="3":
        update_sampah()
        jeda()
    elif opsi_kelola_sampah =="4":
        delete_sampah()
        jeda()
    elif opsi_kelola_sampah == "5":
        leave_akun()

def read_sampah():
    print("==DAFTAR PENERIMAAN SAMPAH==")
    print("=========BANK SIGAM=========")
    for i in range(len(daftar_sampah)):
        print(
        i + 1, ".",
        daftar_sampah[i][0],
        "- Rp", daftar_sampah[i][1], "/Kg"
        )

def create_sampah():
    print("==TAMBAHKAN JENIS DAN HARGA SAMPAH==")
    jenis_sampah = input("Masukkan jenis sampah: ").strip()
    if jenis_sampah == "":
        print("Masukkan jenis sampah, tidak boleh kosong")
    else:
        tersedia = False
        for sampah in daftar_sampah:
            if sampah[0].lower() == jenis_sampah.lower():
                tersedia = True
                break
        if tersedia:
            print("Jenis sampah sudah terdaftar")
        else:
            harga_sampah = input("Masukkan harga per Kg: ")
            if harga_sampah.isdigit() and int(harga_sampah) > 0:
                daftar_sampah.append(
                    [jenis_sampah, int(harga_sampah)]
                )
                print("Jenis sampah berhasil ditambahkan")
            else:
                print("Harga harus berbentuk angka dan bernilai positif")

def update_sampah():
    print("==PERBARUI HARGA SAMPAH==")
    read_sampah()
    pilihan = input("Pilih nomor sampah untuk memperbarui harga: ")
    if pilihan.isdigit():
        nomor_sampah = int(pilihan) - 1
        if 0 <= nomor_sampah < len(daftar_sampah):
            print(daftar_sampah[nomor_sampah][0])
            harga_baru = input("Masukkan harga baru: ")
            if harga_baru.isdigit() and int(harga_baru) > 0:
                daftar_sampah[nomor_sampah][1] = int(harga_baru)
                print("Harga berhasil diperbarui")
            else:
                print("Harga harus berbentuk angka dan positif")
        else:
            print("Nomor sampah tidak ditemukan")
    else:
        print("Masukkan nomor sampah yang terdaftar")

def delete_sampah():
    print("==HAPUS PENERIMAAN SAMPAH==")
    read_sampah()
    pilihan = input("Pilih nomor sampah untuk dihapus: ")
    if pilihan.isdigit():
        nomor_hapus = int(pilihan) - 1
        if 0 <= nomor_hapus < len(daftar_sampah):
            hapus = daftar_sampah.pop(nomor_hapus)
            print(hapus[0], "berhasil dihapus")
        else:
            print("Nomor sampah tidak ditemukan")
    else:
        print("Masukkan nomor sampah yang terdaftar")

def opsiA2():
    os.system("cls")
    print("===MENU KELOLA DATA NASABAH===")
    print("1. Data Nasabah")
    print("2. Riwayat Transaksi Nasabah")
    print("3. Update Data Nasabah")
    print("4. Hapus Data Nasabah")
    print("5. Cari Nasabah")
    print("6. Exit akun")
    opsi_kelola_nasabah = input("Masukkan opsi (1-6): ")
    while opsi_kelola_nasabah not in ("1", "2", "3", "4", "5", "6"):
        print("Opsi keliru. Masukkan angka menu 1-6")
        opsi_kelola_nasabah = input("Masukkan opsi (1-6): ")
    if opsi_kelola_nasabah == "1":
        read_nasabah()
        jeda()
    elif opsi_kelola_nasabah == "2":
        read_riwayat()
        jeda()
    elif opsi_kelola_nasabah == "3":
        update_nasabah()
        jeda()
    elif opsi_kelola_nasabah == "4":
        delete_nasabah()
        jeda()
    elif opsi_kelola_nasabah == "5":
        read_nasabah_user()
        jeda()
    elif opsi_kelola_nasabah == "6":
        leave_akun()
        

def read_nasabah():
    print("==DATA NASABAH==")
    data_nasabah = False
    for user in data_user:
        if data_user[user]["Status"] == "Nasabah":
            data_nasabah = True
            print("Username:", user)
            print("Nama:", data_user[user]["Nama"])
            print("Saldo: Rp", data_user[user]["Saldo"])
            print("----------------------")
    if not data_nasabah:
        print("Belum ada nasabah terdaftar")

def read_riwayat():
    print("==RIWAYAT TRANSAKSI NASABAH==")
    read_nasabah()
    pilihan_username = input("Masukkan username nasabah: ")
    if pilihan_username in data_user and data_user[pilihan_username]["Status"] == "Nasabah":
        riwayat = data_user[pilihan_username]["Riwayat Transaksi"]
        print()
        print("==RIWAYAT TRANSAKSI:", pilihan_username,"==")
        if len(riwayat) == 0:
            print("Belum ada transaksi")
        else:
            for i in range(len(riwayat)):
                print("Transaksi", i + 1)
                print("Jenis sampah:", riwayat[i][0])
                print("Harga per Kg: Rp", riwayat[i][1])
                print("Berat:", riwayat[i][2], "Kg")
                print("Total: Rp", riwayat[i][3])
                print("----------------------")
    else:
        print("Username nasabah tidak ditemukan")

def update_nasabah():
    print("==UPDATE DATA NASABAH==")
    read_nasabah()
    username_lama = input("Masukkan username nasabah: ")
    if username_lama in data_user and data_user[username_lama]["Status"] == "Nasabah":
        print("Silahkan mengosongkan input jika tidak ingin mengubah data (Enter)")
        username_baru = input("Username baru: ").strip()
        if username_baru == "":
            username_baru = username_lama
        if username_baru != username_lama and username_baru in data_user:
            print("Username sudah digunakan")
        else:
            nama_terbaru = input("Nama baru: ").strip()
            password_terbaru = input("Password baru: ").strip()
            if nama_terbaru != "":
                data_user[username_lama]["Nama"] = nama_terbaru
            if password_terbaru != "":
                data_user[username_lama]["Password"] = password_terbaru
            if username_baru != username_lama:
                data_user[username_baru] = data_user[username_lama]
                del data_user[username_lama]
            print("Data nasabah berhasil diperbarui")
    else:
        print("Username nasabah tidak ditemukan")

def delete_nasabah():#
    print("==HAPUS DATA NASABAH==")
    read_nasabah()
    hapus_username = input("Masukkan username nasabah untuk dihapus: ")
    if hapus_username in data_user and data_user[hapus_username]["Status"] == "Nasabah":
        konfirmasi = input("Hapus seluruh data nasabah ini (y/n)?: ").lower()
        while konfirmasi not in ("y", "n"):
            print("Opsi keliru. Masukkan y atau n")
            konfirmasi = input("Hapus seluruh data nasabah ini (y/n)?: ").lower()
        if konfirmasi == "y":
            del data_user[hapus_username]
            print("Data nasabah berhasil dihapus")
        else:
            print("Penghapusan dibatalkan")
    else:
        print("Username nasabah tidak ditemukan")

def read_user_nasabah(username):
    if username in data_user:
        if data_user[username]["Status"] == "Nasabah":
            return data_user[username]
    return None

def read_nasabah_user():
    find_username = input("Masukkan username nasabah yang ingin dicari: ")
    hasil = read_user_nasabah(find_username)
    if hasil is not None:
        print("Nama:", hasil["Nama"])
        print("Saldo:", hasil["Saldo"])
    else:
        print("Data nasabah tidak ditemukan.")

def menu_nasabah():
    os.system("cls")
    print("===MENU NASABAH===")
    print("1. Data Saya")
    print("2. Daftar Penerimaan Sampah")
    print("3. Tukar Sampah")
    print("4. Riwayat Transaksi")
    print("5. Exit akun")
    opsi_nasabah = input("Masukkan opsi (1-5): ")
    while opsi_nasabah not in ("1", "2", "3", "4", "5"):
        print("Opsi keliru. Masukkan angka menu 1-5")
        opsi_nasabah = input("Masukkan opsi (1-5): ")
    if opsi_nasabah == "1":
        read_user()
        jeda()
    elif opsi_nasabah == "2":
        read_sampah()
        jeda()
    elif opsi_nasabah == "3":
        trade_sampah()
        jeda()
    elif opsi_nasabah == "4":
        read_riwayat_user()
        jeda()
    elif opsi_nasabah == "5":
        leave_akun()

def read_user():
    print("==DATA SAYA==")
    print("Username:", pengguna)
    print("Nama:", data_user[pengguna]["Nama"])
    print("Saldo: Rp", data_user[pengguna]["Saldo"])

def trade_sampah():
    print("==MENU PENUKARAN SAMPAH==")
    read_sampah()
    pilihan = input("Pilih jenis sampah untuk ditukar: ")
    if pilihan.isdigit() and 1 <= int(pilihan) <= len(daftar_sampah):
        nomor = int(pilihan) - 1
        jenis = daftar_sampah[nomor][0]
        harga = daftar_sampah[nomor][1]
        input_berat = input("Masukkan berat sampah (Kg): ")
        if input_berat.isdigit() and int(input_berat) > 0:
            berat = int(input_berat)
            total = hitung_total(harga, berat)
            print()
            print("==RINCIAN PENUKARAN==")
            print("Jenis sampah:", jenis)
            print("Harga per Kg: Rp", harga)
            print("Berat:", berat, "Kg")
            print("Total diterima: Rp", total)
            print()
            konfirmasi = input("Lanjutkan penukaran (y/n)?: ").lower()
            while konfirmasi not in ("y", "n"):
                print("Opsi keliru. Masukkan y atau n")
                konfirmasi = input("Lanjutkan penukaran (y/n)?: ").lower()
            if konfirmasi == "y":
                data_user[pengguna]["Saldo"] += total
                data_user[pengguna]["Riwayat Transaksi"].append(
                    [jenis, harga, berat, total]
                )
                print("Penukaran berhasil")
                print("Saldo sekarang: Rp",
                    data_user[pengguna]["Saldo"])
            else:
                print("Penukaran dibatalkan")
        else:
            print("Berat harus berbentuk angka dan bernilai positif")
    else:
        print("Pilihan jenis sampah tidak valid")

def hitung_total(harga, berat):
    return harga * berat

def read_riwayat_user():
    riwayat = data_user[pengguna]["Riwayat Transaksi"]
    print("==RIWAYAT TRANSAKSI==")
    if len(riwayat) == 0:
        print("Belum ada transaksi")
    else:
        for i in range(len(riwayat)):
            print("Transaksi", i + 1)
            print("Jenis sampah:", riwayat[i][0])
            print("Harga per Kg: Rp", riwayat[i][1])
            print("Berat:", riwayat[i][2], "Kg")
            print("Total diterima: Rp", riwayat[i][3])
            print("----------------------")

import os
os.system("cls")

data_user = {
    "Kucing": {
        "Nama" : "Kamil",
        "Password" : "6402",
        "Saldo" : 0,
        "Status" : "Admin",
        "Riwayat Transaksi" : []
    },
}
daftar_sampah = []
pengguna = None
program = True
while program:
    menu_utama()

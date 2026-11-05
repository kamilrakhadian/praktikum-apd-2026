import os
from storage import data_user, daftar_sampah
from tools import jeda, leave_akun, input_konfirmasi
from prettytable import PrettyTable

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
        return opsiA1()
    elif opsi_admin == "2":
        return opsiA2()
    elif opsi_admin == "3":
        return leave_akun()
    return False

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
        return leave_akun()
    return False

def read_sampah():
    print("==DAFTAR PENERIMAAN SAMPAH==")
    print("=========BANK SIGAM=========")
    if len(daftar_sampah) == 0:
        print("Belum ada jenis sampah terdaftar")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Jenis Sampah", "Harga / Kg"]
        for i in range(len(daftar_sampah)):
            tabel.add_row([
                i + 1,
                daftar_sampah[i][0],
                "Rp " + format(daftar_sampah[i][1], ",").replace(",", ".")
            ])
        print(tabel)

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
        return leave_akun()
    return False

def read_nasabah():
    print("==DATA NASABAH==")
    data_nasabah = False
    tabel = PrettyTable()
    tabel.field_names = ["No", "Username", "Nama", "Saldo"]
    nomor = 1
    for user in data_user:
        if data_user[user]["Status"] == "Nasabah":
            data_nasabah = True
            tabel.add_row([
                nomor,
                user,
                data_user[user]["Nama"],
                "Rp " + format(data_user[user]["Saldo"], ",").replace(",", ".")
            ])
            nomor += 1
    if data_nasabah:
        print(tabel)
    else:
        print("Belum ada nasabah terdaftar")

def read_riwayat():
    print("==RIWAYAT TRANSAKSI NASABAH==")
    read_nasabah()
    pilihan_username = input("Masukkan username nasabah: ").strip()
    if pilihan_username in data_user and data_user[pilihan_username]["Status"] == "Nasabah":
        riwayat = data_user[pilihan_username]["Riwayat Transaksi"]
        print()
        print("==RIWAYAT TRANSAKSI:", pilihan_username,"==")
        if len(riwayat) == 0:
            print("Belum ada transaksi")
        else:
            tabel = PrettyTable()
            tabel.field_names = [
                "No Transaksi", 
                "Jenis Sampah", 
                "Harga / Kg", 
                "Berat (Kg)", 
                "Total"
            ]
            for i in range(len(riwayat)):
                tabel.add_row([
                    i + 1,
                    riwayat[i][0],
                    "Rp " + format(riwayat[i][1], ",").replace(",", "."),
                    riwayat[i][2],
                    "Rp " + format(riwayat[i][3], ",").replace(",", ".")
                ])
            print(tabel)
    else:
        print("Username nasabah tidak ditemukan")

def update_nasabah():
    print("==UPDATE DATA NASABAH==")
    read_nasabah()
    username_lama = input("Masukkan username nasabah: ").strip()
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
            terupdate = False
            if nama_terbaru != "":
                data_user[username_lama]["Nama"] = nama_terbaru
                terupdate = True
            if password_terbaru != "":
                data_user[username_lama]["Password"] = password_terbaru
                terupdate = True
            if username_baru != username_lama:
                data_user[username_baru] = data_user[username_lama]
                del data_user[username_lama]
                terupdate = True

            if terupdate:
                print("Data nasabah berhasil diperbarui")
            else:
                print("Tidak ada perubahan data")
    else:
        print("Username nasabah tidak ditemukan")

def delete_nasabah():#
    print("==HAPUS DATA NASABAH==")
    read_nasabah()
    hapus_username = input("Masukkan username nasabah untuk dihapus: ").strip()
    if hapus_username in data_user and data_user[hapus_username]["Status"] == "Nasabah":
        konfirmasi = input_konfirmasi("Hapus seluruh data nasabah ini (y/n)?: ")
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
    find_username = input("Masukkan username nasabah yang ingin dicari: ").strip()
    hasil = read_user_nasabah(find_username)
    if hasil is not None:
        print("Nama:", hasil["Nama"])
        print("Saldo:", hasil["Saldo"])
    else:
        print("Data nasabah tidak ditemukan.")
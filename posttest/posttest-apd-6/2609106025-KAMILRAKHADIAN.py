
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
while(True):
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
                    else:
                        print("Password salah, coba lagi")
                if success:
                    pengguna = username
                    while pengguna != None:
                        if data_user[username]["Status"] == "Admin":
                            os.system("cls")
                            print("===MENU ADMIN===")
                            print("1. Kelola Sampah")
                            print("2. Kelola Data Nasabah")
                            opsi_admin = input("Masukkan opsi (1/2): ")
                            while opsi_admin not in ("1", "2"):
                                print("Opsi keliru. Masukkan angka menu 1 atau 2")
                                opsi_admin = input("Masukkan opsi (1/2): ")
                            if opsi_admin == "1":
                                os.system("cls")
                                print("===MENU KELOLA SAMPAH===")
                                print("1. Daftar Sampah")
                                print("2. Tambah Jenis dan Harga Sampah")
                                print("3. Update Harga Sampah")
                                print("4. Hapus Sampah")
                                opsi_kelola_sampah = input("Masukkan opsi (1-4): ")
                                while opsi_kelola_sampah not in ("1", "2", "3", "4"):
                                    print("Opsi keliru. Masukkan angka menu 1-4")
                                    opsi_kelola_sampah = input("Masukkan opsi (1-4): ")
                                    
                                if opsi_kelola_sampah == "1":
                                    print("==DAFTAR PENERIMAAN SAMPAH==\n""BANK SIGAM")
                                    for i in range(len(daftar_sampah)):
                                        print(
                                            i + 1, ".",
                                            daftar_sampah[i][0],
                                            "- Rp", daftar_sampah[i][1], "/Kg"
                                        )
                                elif opsi_kelola_sampah == "2":
                                    print("==TAMBAHKAN JENIS DAN HARGA SAMPAH==")
                                    jenis_sampah = input("Masukkan jenis sampah: ").strip()
                                    if jenis_sampah == "":
                                        print("Masukkan jenis sampah, tidak boleh kosong")
                                    else:
                                        tersedia = False
                                        for sampah in daftar_sampah:
                                            if sampah[0].lower() == jenis_sampah.lower():
                                                tersedia = True
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

                                elif opsi_kelola_sampah == "3":
                                    print("==PERBARUI HARGA SAMPAH==")
                                    for i in range(len(daftar_sampah)):
                                        print(
                                            i + 1, ".",
                                            daftar_sampah[i][0],
                                            "- Rp", daftar_sampah[i][1], "/Kg"
                                        )
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

                                elif opsi_kelola_sampah == "4":
                                    print("==HAPUS PENERIMAAN SAMPAH==")
                                    for i in range(len(daftar_sampah)):
                                        print(
                                            i + 1, ".",
                                            daftar_sampah[i][0],
                                            "- Rp", daftar_sampah[i][1], "/Kg"
                                        )
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

                                
                            elif opsi_admin == "2":
                                os.system("cls")
                                print("===MENU KELOLA DATA NASABAH===")
                                print("1. Data Nasabah")
                                print("2. Riwayat Transaksi Nasabah")
                                print("3. Update Data Nasabah")
                                print("4. Hapus Data Nasabah")
                                opsi_kelola_nasabah = input("Masukkan opsi (1-4): ")
                                while opsi_kelola_nasabah not in ("1", "2", "3", "4"):
                                    print("Opsi keliru. Masukkan angka menu 1-4")
                                    opsi_kelola_nasabah = input("Masukkan opsi (1-4): ")

                                if opsi_kelola_nasabah == "1":
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

                                if opsi_kelola_nasabah == "2":
                                    print("==RIWAYAT TRANSAKSI NASABAH==")
                                    print("=======DAFTAR NASABAH=======")
                                    for user in data_user:
                                        if data_user[user]["Status"] == "Nasabah":
                                            print("Username:", user)
                                            print("Nama:", data_user[user]["Nama"])
                                            print("----------------------")
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

                                if opsi_kelola_nasabah == "3":
                                    print("==UPDATE DATA NASABAH==")
                                    print("====DAFTAR NASABAH====")
                                    for user in data_user:
                                        if data_user[user]["Status"] == "Nasabah":
                                            print("Username:", user)
                                            print("Nama:", data_user[user]["Nama"])
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
                                            if password_baru != "":
                                                data_user[username_lama]["Password"] = password_terbaru
                                            if username_baru != username_lama:
                                                data_user[username_baru] = data_user[username_lama]
                                                del data_user[username_lama]
                                            print("Data nasabah berhasil diperbarui")
                                    else:
                                        print("Username nasabah tidak ditemukan")

                                if opsi_kelola_nasabah == "4":
                                    print("==HAPUS DATA NASABAH==")
                                    print("====DAFTAR NASABAH====")
                                    for user in data_user:
                                        if data_user[user]["Status"] == "Nasabah":
                                            print("Username:", user)
                                            print("Nama:", data_user[user]["Nama"])
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

                            leave_akun = input("Keluar dari akun (y/n)? ").lower()
                            while leave_akun not in ("y", "n"):
                                print("Opsi keliru. Masukkan y atau n")
                                leave_akun = input("Keluar dari akun (y/n)?: ").lower()
                            if leave_akun == "y":
                                print("Anda telah log out.")
                                pengguna = None
                                break
                        else:
                            os.system("cls")
                            print("===MENU NASABAH===")
                            print("1. Data Saya")
                            print("2. Daftar Penerimaan Sampah")
                            print("3. Tukar Sampah")
                            print("4. Riwayat Transaksi")
                            opsi_nasabah = input("Masukkan opsi (1-4): ")
                            while opsi_nasabah not in ("1", "2", "3", "4"):
                                print("Opsi keliru. Masukkan angka menu 1-4")
                                opsi_nasabah = input("Masukkan opsi (1-4): ")

                            if opsi_nasabah == "1":
                                print("==DATA SAYA==")
                                print("Username:", pengguna)
                                print("Nama:", data_user[pengguna]["Nama"])
                                print("Saldo: Rp", data_user[pengguna]["Saldo"])
                            
                            elif opsi_nasabah == "2":
                                print("==DAFTAR PENERIMAAN SAMPAH==")
                                print("=========BANK SIGAM=========")
                                for i in range(len(daftar_sampah)):
                                    print(
                                    i + 1, ".",
                                    daftar_sampah[i][0],
                                    "- Rp", daftar_sampah[i][1], "/Kg"
                                    )

                            elif opsi_nasabah == "3":
                                print("==MENU PENUKARAN SAMPAH==")
                                for i in range(len(daftar_sampah)):
                                    print(
                                        i + 1, ".",
                                        daftar_sampah[i][0],
                                        "- Rp", daftar_sampah[i][1], "/Kg"
                                    )
                                pilihan = input("Pilih jenis sampah untuk ditukar: ")
                                if pilihan.isdigit() and 1 <= int(pilihan) <= len(daftar_sampah):
                                    nomor = int(pilihan) - 1
                                    jenis = daftar_sampah[nomor][0]
                                    harga = daftar_sampah[nomor][1]
                                    input_berat = input("Masukkan berat sampah (Kg): ")
                                    if input_berat.isdigit() and int(input_berat) > 0:
                                        berat = int(input_berat)
                                        total = harga * berat
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

                            elif opsi_nasabah == "4":
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

                            leave_akun = input("Keluar dari akun (y/n)?: ").lower()
                            while leave_akun not in ("y", "n"):
                                print("Opsi keliru. Masukkan y atau n")
                                leave_akun = input("Keluar dari akun (y/n)? ").lower()
                            if leave_akun == "y":
                                print("Anda telah log out.")
                                pengguna = None
                                break

            else:
                print("Username tidak ditemukan, silahkan registrasi")
                kembali = input("Kembali ke menu utama (y/n): ").lower()
                while kembali not in ("y", "n"):
                    print("Opsi keliru. Masukkan y atau n")
                    kembali = input("Kembali ke menu utama (y/n): ").lower()
                while kembali == "n":
                    print("Untuk melanjutkan ke registrasi, kembali ke menu utama")
                    kembali = input("Kembali ke menu utama (y/n): ").lower()
                if kembali == "y":
                    continue

            
    elif opsi == "2":
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
        continue

    elif opsi == 3:
        break

    leave_system = input("Keluar dari sistem (y/n)? : ").lower()
    while leave_system not in ("y", "n"):
        print("Opsi keliru. Masukkan y atau n")
        leave_system = input("Keluar dari sistem (y/n)?: ").lower()
    if leave_system == "y":
        print("Anda telah keluar dari sistem")
        break
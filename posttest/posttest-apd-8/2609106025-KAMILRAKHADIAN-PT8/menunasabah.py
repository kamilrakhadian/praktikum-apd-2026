import os
from storage import data_user, daftar_sampah
from tools import jeda, leave_akun, input_konfirmasi
from menuadmin import read_sampah
from prettytable import PrettyTable

def menu_nasabah(pengguna):
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
        read_user(pengguna)
        jeda()
    elif opsi_nasabah == "2":
        read_sampah()
        jeda()
    elif opsi_nasabah == "3":
        trade_sampah(pengguna)
        jeda()
    elif opsi_nasabah == "4":
        read_riwayat_user(pengguna)
        jeda()
    elif opsi_nasabah == "5":
        return leave_akun()
    return False

def read_user(pengguna):
    print("==DATA SAYA==")
    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Informasi"]
    tabel.add_row(["Username", pengguna])
    tabel.add_row(["Nama", data_user[pengguna]["Nama"]])
    tabel.add_row(["Saldo", "Rp " + format(data_user[pengguna]["Saldo"], ",").replace(",", ".")])
    print(tabel)

def trade_sampah(pengguna):
    print("==MENU PENUKARAN SAMPAH==")
    read_sampah()
    if len(daftar_sampah) == 0:
        return
    pilihan = input("Pilih nomor jenis sampah untuk ditukar: ").strip()
    if pilihan.isdigit() and 1 <= int(pilihan) <= len(daftar_sampah):
        nomor = int(pilihan) - 1
        jenis = daftar_sampah[nomor][0]
        harga = daftar_sampah[nomor][1]
        print("Hanya menerima sampah dengan berat bulat (Kg) dan bernilai positif")
        input_berat = input("Masukkan berat sampah (Kg): ").strip()
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
            konfirmasi = input_konfirmasi("Lanjutkan penukaran (y/n)?: ")
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

def read_riwayat_user(pengguna):
    riwayat = data_user[pengguna]["Riwayat Transaksi"]
    print("==RIWAYAT TRANSAKSI==")
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
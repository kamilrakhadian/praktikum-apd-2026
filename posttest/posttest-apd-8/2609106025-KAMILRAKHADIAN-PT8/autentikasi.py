import os

from storage import data_user
from tools import jeda

def opsi1():
    os.system("cls")
    print("==Silahkan Login==")
    username = input("Masukkan username anda: ").strip()
    if username in data_user:
        percobaan = 0
        max_percobaan = 3
        while percobaan < max_percobaan:
            password_nasabah = input("Masukkan password anda: ").strip()
            if password_nasabah == data_user[username]["Password"]:
                os.system("cls")
                print("Login berhasil")
                print("Selamat datang,", data_user[username]["Nama"])
                return username
            else:
                percobaan += 1
                if percobaan < max_percobaan:
                    print("Password salah, coba lagi")
                    print("Sisa percobaan:", max_percobaan - percobaan)
                else:
                    print("Kesempatan login habis")
                    jeda()
    else:
        print("Username tidak ditemukan, silahkan registrasi terlebih dahulu")
        jeda()
    return None
    
def opsi2():
    os.system("cls")
    print("==Silahkan Registrasi==")
    username_baru = input("Buat username: ").strip()
    while username_baru == "" or username_baru in data_user:
        os.system("cls")
        if username_baru == "":
            print("Username tidak boleh kosong")
        else:
            print("Username telah digunakan, coba yang lain")
        username_baru = input("Buat username: ").strip()

    nama_baru = input("Masukkan nama: ").strip()
    while nama_baru == "":
        print("Nama tidak boleh kosong")
        nama_baru = input("Masukkan nama: ").strip()

    password_baru = input("Masukkan password: ").strip()
    while password_baru == "":
        print("Password tidak boleh kosong")
        password_baru = input("Masukkan password: ").strip()

    data_user[username_baru] = {
        "Nama": nama_baru,
        "Password": password_baru,
        "Saldo" : 0,
        "Status" : "Nasabah",
        "Riwayat Transaksi" : []
    }
    print("Anda berhasil registrasi, silahkan login")

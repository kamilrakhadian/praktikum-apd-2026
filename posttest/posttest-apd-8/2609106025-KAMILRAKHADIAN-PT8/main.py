import os
from autentikasi import opsi1, opsi2
from tools import jeda, leave
from menuadmin import menu_admin
from menunasabah import menu_nasabah
from storage import data_user

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

    return opsi

def opsi3():
    global program
    if leave():
        program = False

program = True
while program:
    pilihan = menu_utama()
    if pilihan == "1":
        pengguna = opsi1()
        if pengguna is not None:
            while pengguna is not None:
                if data_user[pengguna]["Status"] == "Admin":
                    keluar_akun = menu_admin()
                elif data_user[pengguna]["Status"] == "Nasabah":
                    keluar_akun = menu_nasabah(pengguna)
                if keluar_akun:
                    pengguna = None
    elif pilihan == "2":
        opsi2()
        jeda()
    elif pilihan == "3":
        opsi3()

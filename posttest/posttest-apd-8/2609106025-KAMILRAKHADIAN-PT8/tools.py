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
    leave_account = input_konfirmasi("Keluar dari akun (y/n)? : ")
    if leave_account == "y":
        print("Anda telah log out.")
        return True
    return False

def jeda():
    input("\nTEKAN ENTER UNTUK MELANJUTKAN")
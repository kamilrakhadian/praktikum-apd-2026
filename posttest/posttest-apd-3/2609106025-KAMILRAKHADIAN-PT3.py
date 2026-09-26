# Buatlah program Python untuk mensimulasikan transaksi pengisian BBM di SPBU menggunakan percabangan !
#Login
nama_p = "KAMIL"
nim2 = 25 
#BBM
pertalite = 10000
pertamax = 12500
pertamax_turbo = 15000
bbm = [pertalite, pertamax, pertamax_turbo]
jenis_bbm = ["Pertalite", "Pertamax", "Pertamax Turbo"]
#diskon
diskon1 = 0.1
diskon2 = 0.05
diskon3 = 0
diskon = [diskon1, diskon2, diskon3]
diskonm = 0.02
#Start
nama = input("Masukkan nama panggilan : ").upper()
nim2 = input("Masukkan 2 digit terakhir NIM : ")
if nama == nama_p and nim2 == str(nim2):
    print("Selamat datang ", nama)
    print("NIM = ", nim2)
else:
    print("Maaf, nama atau NIM salah!")
    exit()
print("Silahkan pilih menu BBM dengan angka yang tersedia")
print("1. Pertalite         = Rp. 10.000/liter")
print("2. Pertamax          = Rp. 12.500/liter")
print("3. Pertamax Turbo    = Rp. 15.000/liter")
BBM = input("Masukkan pilihan BBM (1/2/3): ")
liter = int(input("Masukkan jumlah liter : "))
print("Pilihan BBM anda adalah : ", BBM, "-", jenis_bbm[int(BBM)-1])
print("Jumlah liter yang diisi : ", liter)
total_harga = liter * bbm[int(BBM)-1]
print("Total harga : Rp. ", total_harga)
if liter >= 10:
    diskon = diskon[0]
elif liter >= 5:
    diskon = diskon[1]
else:
    diskon = diskon[2]
print("Diskon yang didapatkan: ", diskon * 100, "%")
diskon_h = diskon * total_harga
total_bayar = total_harga - diskon_h
print("Total harga : ", int(total_bayar)) 
diskon_member = input("Apakah anda memiliki member? (y/n): ")
if diskon_member == "y":
    diskon_m1 = 0.02
    diskon_m2 = diskon_m1 * total_harga
    diskon_g = diskon_m2 + diskon_h
    print("Diskon yang didapatkan member: ", int((diskon_m1 + diskon) * 100), "%")
    total_bayar_akhir = total_harga - diskon_g
    print("Total harga setelah diskon member: ", int(total_bayar_akhir)) 
else:
    print("=========== STRUK PENGISIAN ===========")
    print("Nama Pelanggan     : ", nama)
    print("NIM                : ", nim2)
    print("Jenis BBM          : ", jenis_bbm[int(BBM)-1])
    print("Jumlah Liter       : ", liter)
    print("Total Harga        : Rp.", int(total_harga))
    print("Diskon             : ", int(diskon * 100), "%")
    print("Total Bayar        : Rp.", int(total_bayar))
    exit()

print("=========== STRUK PENGISIAN ===========")
print("Nama Pelanggan     : ", nama)
print("NIM                : ", nim2)
print("Jenis BBM          : ", jenis_bbm[int(BBM)-1])
print("Jumlah Liter       : ", liter)
print("Total Harga        : Rp.", int(total_harga))
print("Diskon + Member    : ", int((diskon_m1 + diskon) * 100), "%")
print("Total Bayar        : Rp.", int(total_bayar_akhir))
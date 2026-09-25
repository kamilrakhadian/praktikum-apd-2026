# # print("Hello")
# # print("Miaw Miaw Miaw") 

diskon1 = 0.1
diskon2 = 0.05
diskon3 = 0
diskon = [diskon1, diskon2, diskon3]
liter = int(input("Masukkan jumlah liter: "))
if liter >= 10:
    diskon = diskon[0]
elif liter >= 5:
    diskon = diskon[1]
else:
    diskon = diskon[2]
print("Diskon yang didapatkan: ", diskon * 100, "%")
total_harga = liter * 10000
diskon_h = diskon * total_harga
total_bayar = total_harga - diskon_h
print("Total harga yang harus dibayar: ", int(total_bayar)) 
diskon_member = input("Apakah anda member? (y/n): ")
if diskon_member == "y":
    diskon_m1 = 0.02
    diskon_m2 = diskon_m1 * total_harga
    diskon_g = diskon_m2 + diskon_h
    print("Diskon yang didapatkan member: ", int((diskon_m1 + diskon) * 100), "%")
    total_bayar_akhir = total_harga - diskon_g
    print("Total harga setelah diskon member: ", int(total_bayar_akhir)) 
else:
    print("Terima kasih telah berbelanja di toko kami!")
    print("Diskon yang didapatkan           : ", diskon * 100, "%")
    print("Total harga yang harus dibayar   : ", int(total_bayar)) 
    exit()

print("Terima kasih telah berbelanja di toko kami!")
print("Diskon yang didapatkan               : ", diskon * 100, "%")
print("Total harga yang harus dibayar       : ", int(total_bayar)) 
print("Diskon yang didapatkan member        : ", int((diskon_m1 + diskon) * 100), "%")
print("Total harga setelah diskon member    : ", int(total_bayar_akhir))
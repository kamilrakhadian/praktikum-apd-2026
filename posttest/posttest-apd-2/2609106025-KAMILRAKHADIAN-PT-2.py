print("Maskapai Penerbangan ROC")
bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10
bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]
total_berat = bagasi_1 + bagasi_2 + bagasi_3 + bagasi_4 + bagasi_5 + bagasi_6
print("Total berat bagasi = ", total_berat, "Kg")
total_berat_g = total_berat * 1000
total_bayar = int(5/100 * total_berat_g)
print("Total kompensasi yang harus dibayar =", "Rp", total_bayar)
total_berat_akhir = total_berat + total_bayar / 1000
print("Total berat akhir bagasi =", total_berat_akhir, "Kg")
rata_rata = total_berat_akhir / len (bagasi) 
print("Rata-rata berat bagasi =", rata_rata, "Kg")  # Contoh nilai rata-rata, bisa diubah sesuai kebutuhan
NIM = int(input("Masukan 2 Digit Terakhir NIM: "))
if NIM < rata_rata:
    print("Nilai bolean True")
else:
    print("Nilai bolean False")
bagasi_t = bagasi [2:5]
print("Berat bagasi penumpang bagian tengah =", bagasi_t)
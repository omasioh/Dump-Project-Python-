# Timbangan Beras Digital

#jumlah_karung = int(input("Masukkan jumlah karung: "))
#total_berat = 0
#
#for i in range (jumlah_karung):
#    berat_karung = float(input(f"Masukkan berat karung ke-{i+1}: "))
#    total_berat = total_berat + berat_karung

#print(f"total berat karung : {total_berat}")

#Pencatatan liter bensin

Jumlah_kendaraan = int(input("Masukkan jumlah kendaraan: "))
total_liter = 0

for i in range (Jumlah_kendaraan) :
    total_bensin = float(input(f"masukkan biaya bensin per kendaraan ke{i+1}: "))
    total_liter = total_liter + total_bensin

print(f"berikut total liter : {total_liter}")
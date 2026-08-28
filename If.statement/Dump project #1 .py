#Sistem pemrosesan voucher diskon otomatis

nama = input("Masukkan nama anda: ")
total_belanja = input(f"Masukkan total belanja anda: ")
voucher = input("Masukkan voucher: ").upper()
total_diskon = 0 

if nama == "":
    print("Tolong masukkan nama anda")
    exit ()
elif total_belanja == "":
    print("Tolong masukkan total_belanja anda")
    exit ()
elif voucher == "":
    print("Tolong masukkan voucher anda")
    exit ()
elif not total_belanja.isdigit ():
    print("Error = Total belanja tidak boleh alphabet")
    exit ()
else : 
    total_belanja = int(total_belanja)


if total_belanja > 50000 and voucher == "HEMAT50" :
    total_diskon = total_belanja * 0.5
    print("Syarat terpenuhi")
    print(f"Total belanja {total_diskon}")
    if total_diskon > 300000 and voucher == "HEMAT50" :
            total_diskon = 300000
            print("total_belanja melebihi kapasitas")
            print(f"Total belanja {total_diskon}")
elif total_belanja > 50000 and not voucher == "HEMAT50" :
    print("Voucher anda salah")
    print(f"Total belanja {total_belanja}")
elif total_belanja < 50000 and not voucher == "HEMAT50" :
    print("Minimal belanja dan voucher salah")
    print(f"Total belanja {total_belanja}")
elif total_belanja < 50000 and voucher == "HEMAT50":
    print("Minimal belanja untuk menggunakan voucher tak memenuhi")
    print(f"Total belanja {total_belanja}")

if total_belanja > 20000 : 
    ongkir = 0
else :
    ongkir = 2500

total_akhir = (total_belanja - total_diskon) + ongkir

print("Struk")
print(f"nama = {nama}")
print(f"total belanja = {total_belanja}")
print(f"setelah diskon = {total_diskon}")
print(f"ongkos kirim = {ongkir}")
print(f"total akhir = {total_akhir}")
print("Terimakasih telah berbelanja di toko kami")
#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
    # Base case
 
    if len(hasil) == n:  # Jika panjang hasil sudah sama dengan jumlah 'n' yang diminta,
        print(hasil)     # maka cetak hasilnya dan menghentikan rekusri (return)
        return 
    # Recursive case
    #program akan mencoba dua cabang kemungkinan 
    kombinasi(n, hasil + "A")  # cabang 1 : menambahkan huruf A ke dalam hasil
    kombinasi(n, hasil + "B")  # cabang 2 : menambahkan huruf B ke dalam hasil
    
#Menjalankan fungsi untuk mencari kombinasi huruf dengan panjang 2
kombinasi(2)
# Output yang dihasilkan: AA, AB, BA, BB
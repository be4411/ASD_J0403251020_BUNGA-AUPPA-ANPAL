#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0): 
 
    # Base case 
    if index == len(data) - 1: # kondisi  ini tercapai kalau sudah sampai di elemen terakhir dari list
        return data[index]     # karena ga ada angka lain buat dibandingkan, maka angka terakhir itu yang dianggap sebagai nilai max sementara untuk dikembalikan ke atas
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) # Fungsi memanggil dirinya sendiri  dengan menaikan nilai index (+1)
                                           # ini mencari nilai max di sisa list
    if data[index] > maks_sisa: # fungsi membandingkan elemen saat ini dengan nilai max dari sisa list tadi
         # kalau nilai dari sisa list ternyata lebih besar, kembalikan elemen ini
        return data[index] 
    else: 
        # kalau tidak, kembalikan nilai max dari sisa list tadi
        return maks_sisa
 
 
angka = [3, 7, 2, 9, 5]  #ini data yang akan di cari nilai max nya

# menampilkan output
# fungsi dimulai dari index 0
print("Nilai maksimum:", cari_maks(angka)) # outputnya 9
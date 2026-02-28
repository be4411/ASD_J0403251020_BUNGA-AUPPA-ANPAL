#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#==========================================================
# Contoh Backtracking
#==========================================================
def biner(n,hasil=""):
    #Base case : jika panjang string sudah n, cetak hasil
    if len(hasil)== n:
        print(hasil)
        return
    #choose +explore : tambah '0'
    biner(n,hasil + "0")
    #choose +explore : tambah '1'
    biner(n,hasil + "1")

biner(3)

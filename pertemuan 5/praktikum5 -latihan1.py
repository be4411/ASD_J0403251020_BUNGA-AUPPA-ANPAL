#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 
def pangkat(a, n): 
# Base case 
    if n == 0: # kondisi berhenti supaya tidak terjadi infinite loop
        return 1 #kalau pangkat (n) sudah mencapai 0, dikembalikan nilai 1
     
    # Recursive case : buat memanggil dirinya sendiri
    return a * pangkat(a,n-1) # mengalikan 'a' dengan hasil fungsi itu sendiri
                              # Nilai 'n' dikurangi 1 di setiap pemanggilan supaya mendekati base case nya
print(pangkat(2, 4)) # Memanggil fungsi untuk menghitung 2 pangkat 4
                     # outputnya adalah 16
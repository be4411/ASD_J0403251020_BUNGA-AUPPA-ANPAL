#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
    # Base case
    # jika panjang string 'hasil' sudah mencapai target (3 digit),
    if len(hasil) == panjang: 
        print("PIN:", hasil)   # mencetak PIN tersebut dan hentikan rekursi di cabang ini
        return 
    # Recursive case dengan perulangan

    for angka in ["0", "1", "2"]: # mencoba setiap angka dari daftar ["0", "1", "2"] untuk posisi saat ini
        # setelah panggilan ini selesai, program akan kembali 
        if angka not in hasil :                          
            buat_pin(panjang, hasil + angka) # dan mencoba angka berikutnya dalam perulangan.
# menjalankan fungsi untuk membuat PIN sepanjang 3 digit menggunakan angka 0-2
# total kemungkinan yang dihasilkan adalah 3^3 = 27 kombinasi
buat_pin(3)

#cara mencegah angka yang sama muncul berulang, adalah dengan menggunakan pengecekan kembali sebelum melakukan pemanggilan rekusif
# dengan -> if angka not in hasil: (dibawah for angka in  ["0", "1", "2"]:)
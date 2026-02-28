#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================

def countdown(n): 
    # Base case 
    if n == 0:      #  kalau n sudah 0, cetak selesai dan berhenti
        print("Selesai") 
        return
     
    # langkah maju :
    print("Masuk:", n)  # dicetak sebelum memanggil dirinya sendiri
    
    # Rekursi : fungsi ini memanggil dirinya sendiri dengan (n,1)
    countdown(n - 1)  # Baris ini menunda eksekusi baris berikutnya sampai pemanggilan ini selesai
    #langkah mundur
    print("Keluar:", n) #Dicetak setelah pemanggilan di atas selesai
                        # Perintah print("Keluar:", n) berada setelah pemanggilan rekursif 
                        # Jadi, perintah tersebut mengantri di memori,
                        # Karena yang terakhir dipanggil adalah n=1 (sebelum 0), 
                        # maka dia yang pertama kali menyelesaikan antriannya dan keluar paling dulu
countdown(3)
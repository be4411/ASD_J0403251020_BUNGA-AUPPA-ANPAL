#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 1 Memahami Kode Program (Insertion Sort)
#===========================================================

def insertion_sort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1

            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1

            data[j + 1] = key

        return data

#Soal:
#1. Mengapa perulangan dimulai dari indeks 1?
#2. Apa fungsi variabel key?
#3. Mengapa digunakan while, bukan for?
#4. Operasi apa yang terjadi di dalam while?

#Jawaban

#1) karena elemen pertama (index =0) di anggap suda terurut

#2) fungsi variabel key disini adalah untuk menyimpan nilai elemen yang mau disisipkan ke posisi yang benar
#3) kalau for digunakan untuk baris luar karena pasti akan memeriksa elemen dari indeks 1 sampai akhir, kalau while digunakan di dalam baris karena tidak tahu seberapa jauh harus mundur ke kiri untuk menyisipkan key tersebut
#4) operasi yang terjadi dalam while adalah 
    #a) operasi pergeseran (shifting) -> memberikan ruang bagi key
    #b) operasi pembaruan indeks (decrementing) -> Menggerakkan penunjuk pencarian satu langkah lebih jauh ke arah kiri
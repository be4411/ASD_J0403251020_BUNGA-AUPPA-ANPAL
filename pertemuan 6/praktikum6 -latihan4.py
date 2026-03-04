#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 4 . Memahami Kode Program (Merge Sort)
#===========================================================



def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

#Soal:
#1. Apa yang dimaksud dengan base case?
#2. Mengapa fungsi memanggil dirinya sendiri?
#3. Apa tujuan fungsi merge()?

#jawab 

#1) base case disini adalah kondisi berhenti dalam sebuah fungsi rekursif, tujuan nya untuk mencegah fungsi memanggil dirinya sendiri terus menerus (mencegah infinite loop)
#2) proses ini disebut rekursi, untuk melakukan tahap pembagian (divide), yaitu membagi daftar data menjadi bagian bagian yang lebih kecil secara berulang untuk mempermudah
#3) tujuan fungsi merge() untuk memanggil fungsi penggabung atau tahap penggabungan

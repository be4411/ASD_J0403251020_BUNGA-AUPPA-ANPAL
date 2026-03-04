#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 5 . Melengkapi Fungsi Merge
#===========================================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
#Soal:
#1. Lengkapi kondisi agar menjadi ascending.
#2. Jelaskan fungsi result.extend().

#jawaban

#2) fungsi dari result.extend() adalah untuk menambahkan sisa elemen dari satu sub-list ke dalam list result setelah yang lainnya diperiksa
   # untuk mengefisiensikan penggabungan tanpa perlu membandingkan satu-persatu
   #  untuk memastikan tidak ada data yang tertinggal dalam proses penggabungan sehingga semua elemen masuk ke daftar baru yang terurut
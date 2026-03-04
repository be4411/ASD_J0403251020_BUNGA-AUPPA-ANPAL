#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 3  : . Tracing Insertion Sort
#===========================================================

def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

data = [5, 2, 4, 6, 1, 3]
insertionSort(data)

#1. Tuliskan isi list setelah iterasi i = 1.
#2. Tuliskan isi list setelah iterasi i = 3.
#3. Berapa kali pergeseran terjadi pada iterasi i = 4?

#jawab :

#1) Hasil: [2, 5, 4, 6, 1, 3]
#2) Hasil: [2, 4, 5, 6, 1, 3]
#3) terjadi 4 kali pergeseran untuk mendapatkan angka 1 di posisi paling awal
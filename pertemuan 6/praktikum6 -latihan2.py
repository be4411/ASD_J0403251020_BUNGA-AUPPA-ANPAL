#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 2 : Melengkapi Potongan Kode
#===========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    data[j+1] = key
    return data

#===========================================================

def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1


        while j >= 0 and data[j] < key: 
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key 

    return data
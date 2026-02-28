#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#==========================================================
#materi rekursif : menjumlahkan elemen list
#===========================================================
def jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0

    #rekursif case
    return data[index] + jumlah_list(data, index+1)

print("=====program penjumlahan====")
print(jumlah_list)
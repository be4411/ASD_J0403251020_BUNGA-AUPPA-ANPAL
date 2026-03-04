#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Insertion sort dengan tracing
#===========================================================

def insertion_sort(data):
    #melihat data awal
    print("data awal:", data)
    print("=" *50)


    #loop mulai dari data ke 2(index array ke 1)
    for i in range(1,len(data)):

        
        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #index terakhir elemen di bagian kiri

        print("iterasi ke-", i)
        print("nilai key =", key)
        print("bagian kiri(terurut):", data[:i])
        print("bagian kanan (belum terurut): ", data[i:])

        #geser 
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #simpan key ke posisi yang benar
        data[j+1] = key

        print("setelah disisipkam :", data)
        print("-"*50)
    return data

angka =[7,8,5,4,2,6]
print("hasil sorting: ", insertion_sort(angka))
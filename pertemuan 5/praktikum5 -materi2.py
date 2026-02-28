#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#==========================================================
#materi rekursif : faktorial
#t
#===========================================================

def hitung(n):
    if n == 0 :
        print("selesai")
        return
    print("masuk:", n)
    hitung(n-1) #rekursif case
    print("keluar", n)
    hitung(n-1) #rekursif
    print("keluar", n)

print("=====program tracing=====")
hitung(3)

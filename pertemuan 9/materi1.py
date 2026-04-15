#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 1 : Membuat Node 
#===========================================================

#class Node 

class Node:
    def __init__(self, data): 
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
    
#membuat root
root = Node("A")

    #menampilkan isi kode
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)


#Pembahasan :
# 1. Node disini didefinisikan sebagai struktur dasar Binary Tree
# 2. Setiap objek dari class Node memiliki tiga atribut utama: 
#    - 'data' buat menyimpan nilai node nya.
#    - 'left' sebagai pointer ke (child) di sebelah kiri.
#    - 'right' sebagai pointer ke (child) di sebelah kanan.
# 3. Baris 'root = Node("A")' merupakan proses pembuatan akar pertama dari Tree.
# 4. Pada tahap ini, 'root.left' dan 'root.right' nilai nya masih 'None' 
#    karena kita belum menambahkan atau menyambungkan node (child) ke node root tersebut.
# 5. Struktur ini memungkinkan kita untuk membangun Tree yang lebih kompleks dengan 
#    menghubungkan node satu ke node lainnya.

#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 3: Traversal Preoder
#===========================================================
class Node:
    def __init__(self, data): 
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi preorder : root ==> left ==> right

def preorder(node) :
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#membuat tree
root = Node("A")

#membuat child level 1
root.left = Node ("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan fungsi preorder nya
print("hasil transversal preorder:")
preorder(root)

#pahami urutan penelusuran nya

# Pembahasan Urutan Penelusuran Preorder:
# 1. Preorder traversal mengikuti prinsip: Kunjungi Root, lalu sub-pohon Kiri, baru sub-pohon Kanan.
# 2. Fungsi 'preorder(node)' bekerja secara rekursif. Jika node tidak kosong (None), 
#    ia akan mencetak data terlebih dahulu sebelum berpindah ke node berikutnya.
# 3. Berdasarkan struktur tree yang dibuat:
#    - Pertama, mencetak 'A' (sebagai root utama).
#    - Lalu masuk ke sisi kiri untuk mencetak 'B'.
#    - Lanjut ke sisi kiri dari B, mencetak 'D'.
#    - Karena 'D' adalah leaf (daun), rekursi kembali ke 'B' dan mengecek sisi kanan, mencetak 'E'.
#    - Setelah sisi kiri root selesai, rekursi kembali ke 'A' dan mengecek sisi kanan, mencetak 'C'.
# 4. Jadi output dari penelusuran ini adalah: A B D E C.
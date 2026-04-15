#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 2 : Membuat Binary Search Tree sederhana
#===========================================================

class Node:
    def __init__(self, data): 
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

root = Node("A")

#membuat child level 1
root.left = Node ("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#child 3
root.right.left = Node("F")
root.right.right = Node("G")

#menampilkan isi kode
print("Data pada root", root.data)
print("Data child kiri root", root.left.data)
print("Data child kanan root", root.right.data)
print("child kiri dari B : ", root.left.left.data)
print("child kanan dari B : ", root.left.right.data)
print("child kiri dari C : ", root.right.left.data)
print("child kanan dari C : ", root.right.right.data)


#lanjutkan kode program untuk keseluruhan

#penjelasan 

# Penjelasan :
# 1. Kode ini mendemonstrasikan pembentukan struktur hirarki Binary Tree secara manual.
# 2. Struktur pohon yang terbentuk adalah:
#          A (Root)
#        /   \
#       B     C (Child Level 1)
#      / \   / \
#     D   E F   G (Child Level 2)
# 3. Setiap node (child) diakses melalui atribut .left atau .right dari parent-nya.
# 4. Contoh: 'root.left.right' merujuk pada node 'E', karena kita bergerak ke 
#    kiri dari A (ke B), lalu ke kanan dari B (ke E).
# 5. Semua node pada level 2 (D, E, F, G) saat ini berstatus sebagai 'Leaf Node' 
#    atau daun, karena mereka belum memiliki anak lagi (left dan right-nya None).
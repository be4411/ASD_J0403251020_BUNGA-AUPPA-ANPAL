#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 6: Struktur organisasi
#===========================================================
class Node:
    def __init__(self, data): 
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

def preorder(node) :
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

root = Node("Direktur")

#child 1

root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child 2
root.left.left = Node("staff 1")
root.left.right = Node("staff 2")

#child 3
root.right.right = Node("staff 3")


print("Struktur Organisasi:")
preorder(root)

#penjelasan : 
#  
# Penjelasan Implementasi Struktur Organisasi:
# 1. Kode ini menerapkan konsep Binary Tree untuk merepresentasikan hirarki jabatan.
# 2. 'Direktur' bertindak sebagai Root (puncak hirarki).
# 3. 'Manajer A' dan 'Manajer B' adalah Child dari Root, mewakili pembagian divisi.
# 4. Penggunaan 'preorder traversal' dalam struktur ini sangat efektif untuk 
#    mendata seluruh anggota organisasi mulai dari jabatan tertinggi hingga 
#    staff di bawahnya secara berurutan per divisi.
# 5. Struktur yang terbentuk:
#    - Direktur
#      /      \
#  Manajer A   Manajer B
#    /   \         \
# staff 1 staff 2  staff 3
# 6. Output yang dihasilkan: Direktur Manajer A staff 1 staff 2 Manajer B staff 3.



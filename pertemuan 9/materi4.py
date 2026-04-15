#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 4:Traversal Inorder
#===========================================================

class Node:
    def __init__(self, data): 
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
#membuat fungsi Inorder left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data,end="")
        inorder(node.right)



#membuat tree
#membuat sebuat node root
root = Node("A")

#membuat child level 1
root.left = Node ("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan fungsi preorder nya
print("hasil transversal inorder:")
inorder(root)

# Pembahasan Urutan Penelusuran Inorder:
# 1. Inorder traversal mengikuti prinsip: Kunjungi sub-pohon Kiri, cetak Root, baru kunjungi sub-pohon Kanan.
# 2. Karakteristik utama Inorder pada Binary Search Tree (BST) biasanya akan menghasilkan 
#    data yang berurutan secara alfabetis atau numerik.
# 3. Berdasarkan struktur tree yang dibuat:
#    - Fungsi akan terus memanggil node.left sampai mencapai node 'D'.
#    - Urutan cetak dimulai dari 'D' (paling kiri), lalu 'B' (parent dari D), kemudian 'E' (kanan dari B).
#    - Setelah sub-pohon kiri selesai, barulah root utama 'A' dicetak.
#    - Terakhir, fungsi mengunjungi dan mencetak sub-pohon kanan yaitu 'C'.
# 4. Hasil akhir penelusuran ini adalah: D B E A C.
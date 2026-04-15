#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
#Latihan 5:Traversal Postorder
#===========================================================

class Node:
    def __init__(self, data): 
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
#membuat traversal postorder :
# left -> right -> root

def postorder(node):
    if node is None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end="")



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
print("hasil transversal postorder:")
postorder(root)

#penjelasan :

# Penjelasan Urutan Penelusuran Postorder:
# 1. Postorder traversal mengikuti prinsip: Kunjungi sub-pohon Kiri, kunjungi sub-pohon Kanan, baru cetak Root.
# 2. Logikanya: Node induk hanya akan dicetak setelah seluruh node anaknya selesai diproses.
# 3. Berdasarkan struktur tree yang dibuat:
#    - Program menelusuri ke titik paling kiri bawah yaitu 'D' dan mencetaknya.
#    - Kemudian menelusuri adik dari D, yaitu 'E', dan mencetaknya.
#    - Setelah D dan E selesai, barulah parent mereka yaitu 'B' dicetak.
#    - Selanjutnya program berpindah ke sisi kanan root utama untuk mencetak 'C'.
#    - Terakhir, root utama 'A' dicetak sebagai penutup.
# 4. Output dari penelusuran ini adalah: D E B C A.
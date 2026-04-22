#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================


# ========================================================== 
# Latihan 4: Membuat BST yang Tidak Seimbang 
# ========================================================== 
 
# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data      # nilai pada node
        self.left = None      # child kiri
        self.right = None     # child kanan


# Fungsi insert untuk BST
# Cara kerjanya rekursif, terus "turun" ke kiri atau kanan
# sampai nemu tempat kosong yang pas buat node baru
def insert(root, data):
    # Jika root kosong, buat node baru
    # Ini kondisi dasarnya — kalau udah sampai tempat kosong, taruh di sini
    if root is None:
        return Node(data)

    # Jika data lebih kecil, masuk ke subtree kiri
    # BST selalu naruh nilai lebih kecil di kiri
    if data < root.data:
        root.left = insert(root.left, data)

    # Jika data lebih besar, masuk ke subtree kanan
    # dan nilai lebih besar di kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    return root  # kembalikan root yang sama (strukturnya sudah diupdate)


# Fungsi preorder untuk melihat bentuk tree
# Urutan preorder: Root-> child Kiri -> child Kanan
# Hasilnya mencerminkan "bentuk" tree dari atas ke bawah
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # cetak node sekarang
        preorder(root.left)        # rekursif ke child kiri
        preorder(root.right)       # rekursif ke child kanan


# Fungsi untuk menampilkan struktur tree
# L = child kiri, R = child kanan, Root = paling atas
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")  # cetak node dengan indentasi
        tampil_struktur(root.left, level + 1, "L")       # turun ke child kiri, level +1
        tampil_struktur(root.right, level + 1, "R")      # turun ke child kanan, level +1


# -----------------------------
# Program utama
# -----------------------------
root = None  # tree masih kosong di awal

# Data dimasukkan berurutan naik
# Karena 10 < 20 < 30, hasilnya tree bakal miring ke kanan semua (tidak seimbang)
data_list = [10, 20, 30]
for data in data_list:
    root = insert(root, data)  # tiap data diinsert satu per satu ke tree

print("Preorder BST:")
preorder(root)  # output: 10 20 30 (root duluan, baru turun ke kanan terus)

print("\n\nStruktur BST:")
tampil_struktur(root)  # keliatan jelas tree-nya lurus ke kanan, gak seimbang

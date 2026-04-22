#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
# Latihan : BST
#===========================================================

# Node adalah "kotak" yang nyimpen satu nilai,
# plus dua pointer ke child kiri dan kanan
class Node:
    def __init__(self, data):
        self.data = data      # nilai yang disimpen di node ini
        self.left = None      # child kiri (awalnya kosong)
        self.right = None     # child kanan (awalnya kosong)


# alur fungsi insert
# Rekursif terus turun ke kiri/kanan sampai nemu tempat kosong
def insert(root, data):
    if root is None:                          # kalau tempatnya kosong, taruh node baru di sini
        return Node(data)

    if data < root.data:                      # kalau data lebih kecil, masuk ke kiri
        root.left = insert(root.left, data)
    elif data > root.data:                    # kalau data lebih besar, masuk ke kanan
        root.right = insert(root.right, data)
                                              # kalau sama persis, diabaikan (gak boleh duplikat)
    return root                               # kembalikan root yang udah diupdate


# mengisi data BST
root = None                                   # tree masih kosong di awal
data_list = [50, 30, 70, 20, 40, 50, 80]     # 50 yang kedua bakal diabaikan karena duplikat

for data in data_list:
    root = insert(root, data)                 # insert satu per satu ke tree

print("BST berhasil dibuat")


#===========================================================
# Latihan2 : Traversal Inorder
#===========================================================

# alur fungsi inorder
# Urutan kunjungan: Kiri -> Root -> Kanan
# Hasilnya selalu urut dari kecil ke besar di BST
def inorder(root):
    if root is not None:
        inorder(root.left)               # kunjungi child kiri dulu (rekursif)
        print(root.data, end=" ")        # cetak nilai node sekarang
        inorder(root.right)              # baru kunjungi child kanan (rekursif)

print("hasil inorder: ")
inorder(root)    # output harusnya: 20 30 40 50 70 80 (urut naik)


#===========================================================
# Latihan 3 : search di BST
#===========================================================

# Fungsi search memanfaatkan sifat BST buat nyari nilai lebih efisien
def search(root, key):
    if root is None:            # sampai ujung tree tapi gak ketemu -> False
        return False
    if root.data == key:        # ketemu -> True
        return True
    elif key < root.data:       # key lebih kecil, cari di subtree kiri
        return search(root.left, key)
    else:                       # key lebih besar, cari di subtree kanan
        return search(root.right, key)

# Uji pencarian
key = 100                       # angka 100 gak ada di data_list, jadi harusnya "tidak ditemukan"

if search(root, key):
    print("data ditemukan")
else:
    print("data tidak ditemukan")






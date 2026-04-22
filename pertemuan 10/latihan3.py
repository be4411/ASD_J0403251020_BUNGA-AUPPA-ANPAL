#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang 
# ========================================================== 
 
# Class Node
# untuk menyimpan data
# sekaligus pointer ke child kiri dan child kanan
class Node:
    def __init__(self, data):
        self.data = data    # nilai yang disimpan di node ini
        self.left = None    # child kiri, awalnya kosong
        self.right = None   # child kanan, awalnya kosong


# Fungsi preorder untuk melihat isi tree
# Urutan preorder: Root -> Kiri -> Kanan
# Berguna buat ngecek isi tree sebelum dan sesudah rotasi
def preorder(root):
    if root is not None:                  # selama node-nya ada (bukan None)
        print(root.data, end=" ")         # cetak nilai node sekarang (Root)
        preorder(root.left)               # lanjut rekursif ke child kiri
        preorder(root.right)              # lanjut rekursif ke child kanan


# Fungsi untuk menampilkan struktur tree
# Nampilin tree secara visual dengan indentasi biar keliatan hierarkinya
# level = seberapa dalam node ini dari root (root = level 0)
# posisi = label apakah node ini Root, child Kiri (L), atau child Kanan (R)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:                                      # kalau node-nya ada
        print("   " * level + f"{posisi}: {root.data}")      # cetak dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L")           # rekursif ke child kiri, level +1
        tampil_struktur(root.right, level + 1, "R")          # rekursif ke child kanan, level +1


# Fungsi rotasi kiri
# Rotasi kiri dipakai kalau tree "berat" di sebelah kanan
# (terlalu panjang ke kanan, seperti kasus 10->20->30 ini)
#
#
# Intinya: child kanan (20) naik jadi root baru,
# dan root lama (10) turun jadi child kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right       # y adalah child kanan x (dalam kasus ini y = 20)
    T2 = y.left       # subtree kiri milik y disimpan sementara
                      # (kalau y punya child kiri, nilainya pasti antara x dan y,
                      #  jadi nanti dipindah jadi child kanan x)

    # Proses rotasi
    y.left = x        # x (10) menjadi child kiri dari y (20)
    x.right = T2      # child kanan x diganti dengan T2
                      # (di kasus ini T2 = None, tapi penting untuk kasus umum)

    # y menjadi root baru
    return y          # kembalikan y (20) sebagai root yang baru


# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
# Semua node masuk ke kanan terus, jadi bentuknya kayak rantai lurus ke kanan
root = Node(10)              # buat root dengan nilai 10
root.right = Node(20)        # 20 langsung ditempel ke kanan 10
root.right.right = Node(30)  # 30 langsung ditempel ke kanan 20

print("Preorder sebelum rotasi kiri:")
preorder(root)               # harusnya keluar: 10 20 30

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)        # keliatan tree miring ke kanan semua

# Melakukan rotasi kiri pada root
# root yang baru adalah node 20 (hasil dari rotate_left)
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)               # harusnya tetap: 10 20 30 (urutan data tidak berubah)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)        # sekarang 20 jadi root, 10 di kiri, 30 di kanan -> seimbang
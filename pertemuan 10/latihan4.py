#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================



# ============================================================
#  Latihan 6 - Rotasi Kanan pada BST Tidak Seimbang
# ============================================================


# CLASS NODE 
# Setiap kotak menyimpan: nilai (data), pointer ke child kiri, dan child kanan.
class Node:
    def __init__(self, data):
        self.data  = data   # nilai yang disimpen di node ini
        self.left  = None   # child kiri (awalnya kosong)
        self.right = None   # child kanan (awalnya kosong)


#   - nilai yang lebih kecil masuk ke KIRI
#   - nilai yang lebih besar masuk ke KANAN
class BST:
    def __init__(self):
        self.root = None  # awalnya tree masih kosong, root belum ada


    # ===INSERT ===
    # Fungsi buat nambahin data ke pohon
    # Panggil fungsi _insert yang rekursif di dalamnya.
    def insert(self, data):
        self.root = self._insert(self.root, data)

    # Fungsi rekursif
    def _insert(self, node, data):
        # Kalau posisi ini kosong, berarti disini node baru diletakkan
        if node is None:
            return Node(data)

        # Kalau data lebih kecil dari node sekarang -> masuk ke kiri
        if data < node.data:
            node.left = self._insert(node.left, data)

        # Kalau data lebih besar -> masuk ke kanan
        elif data > node.data:
            node.right = self._insert(node.right, data)

        # Kalau sama persis, di abaikan
        return node


#===== ROTASI KANAN=====


    def rotasi_kanan(self, node):
        # Kalau nodenya kosong atau gak punya child kiri,
        # rotasi kanan gak bisa dilakukan
        if node is None or node.left is None:
            print("Rotasi kanan gak bisa dilakukan (gak ada child kiri nih).")
            return node

        # Langkah 1: Jadiin child kiri sebagai root baru
        # Dalam kasus ini: new_root = 20
        new_root = node.left

        # Langkah 2: Anak kiri dari node lama (30) diganti dengan
        # child KANAN dari new_root (20).
        # Karena child kanan 20 (kalau ada) nilainya pasti
        # di antara 20 dan 30, jadi tetap valid kalau jadi child kiri 30.
        node.left = new_root.right

        # Langkah 3: Node lama (30) sekarang jadi child KANAN dari new_root (20)
        new_root.right = node

        # Kembalikan root yang baru (yaitu 20)
        return new_root


    #===== TREE ======

    # Dibaca dari bawah ke atas = dari kiri ke kanan tree aslinya.
    # R--- berarti child kanan, L--- berarti child kiri.
    def tampilkan(self, node, level=0, prefix="Root: "):
        if node is not None:
            # Tampilkan child kanan dulu (
            self.tampilkan(node.right, level + 1, "R---")
            # Tampilkan node sekarang dengan indentasi sesuai level
            print(" " * (level * 6) + prefix + str(node.data))
            # Tampilkan child kiri 
            self.tampilkan(node.left, level + 1, "L---")


    # ==== INORDER TRAVERSAL ====
    # Inorder = kunjungi Kiri -> Root -> Kanan
    # Hasilnya selalu urut dari kecil ke besar di BST.
    # Kita pakai ini buat membuktikan kalau rotasi gak mengubah urutan data.
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


# ============================================================
#  PROGRAM UTAMA
# ============================================================

bst  = BST()
data = [30, 20, 10]  # urutan insert 

# Memasukan semua data ke BST satu per satu
for d in data:
    bst.insert(d)

# Tampilkan kondisi tree SEBELUM dirotasi
print("\n>> SEBELUM Rotasi Kanan:")
print("   (Tree tidak seimbang)")
print()
bst.tampilkan(bst.root)
print("\n   Inorder traversal:", end=" ")
bst.inorder(bst.root)
print()

# Lakukan rotasi kanan pada root
# Root baru akan dikembalikan oleh fungsi rotasi_kanan()
bst.root = bst.rotasi_kanan(bst.root)

# Tampilkan kondisi tree SESUDAH dirotasi
print("\n>> SESUDAH Rotasi Kanan:")
print("   ( Tree seimbang!)")
print()
bst.tampilkan(bst.root)
print("\n   Inorder traversal:", end=" ")
bst.inorder(bst.root)
print()


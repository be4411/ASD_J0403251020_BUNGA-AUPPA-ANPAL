#=====================================
# Nama  : Bunga Auppa Anpal
# NIM   : J0403251020
# Kelas : TPL/B2
# Praktikum 13 - Graph III: Spanning Tree
#=========================================

# ==========================================================
# DAFTAR EDGE GRAPH
# ==========================================================

# Graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]


# CONTOH SPANNING TREE


# Spanning tree valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# ==========================================================
# MENAMPILKAN GRAPH
# ==========================================================

print("=== EDGE PADA GRAPH ===")

for edge in edges:
    print(edge)

# ==========================================================
# MENAMPILKAN SPANNING TREE
# ==========================================================

print("\n=== SPANNING TREE ===")

for edge in spanning_tree:
    print(edge)

# ==========================================================
# MENAMPILKAN JUMLAH EDGE
# ==========================================================

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Graph awal memiliki lebih banyak edge dan memiliki cycle,
#    sedangkan spanning tree hanya menggunakan edge yang diperlukan
#    untuk menghubungkan semua node tanpa cycle

# 2. Spanning tree tidak boleh memiliki cycle karena cycle
#    menyebabkan penggunaan edge berlebih dan membuat koneksi
#    menjadi tidak efisien

# 3. Jumlah edge spanning tree lebih sedikit karena spanning tree
#    hanya menggunakan edge minimum untuk menghubungkan semua node
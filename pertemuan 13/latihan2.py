#=====================================
# Nama  : Bunga Auppa Anpal
# NIM   : J0403251020
# Kelas : TPL/B2
# Praktikum 13 - Graph III: Spanning Tree
#=========================================

# ==========================================================
# DAFTAR EDGE
# Format:(bobot, node1, node2)
# ==========================================================

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# ==========================================================
# MENGURUTKAN EDGE BERDASARKAN BOBOT TERKECIL
# ==========================================================

edges.sort()

# List untuk menyimpan MST
mst = []

# Menyimpan total bobot
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# ==========================================================
# PROSES KRUSKAL
# ==========================================================

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))

        total_weight += weight

        connected.add(u)
        connected.add(v)

# ==========================================================
# OUTPUT MST
# ==========================================================

print("=== MINIMUM SPANNING TREE ===")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Edge yang dipilih pertama kali adalah C-D
#    karena memiliki bobot paling kecil yaitu 1

# 2. Edge dengan bobot paling kecil dipilih lebih dahulu
#    agar total bobot MST menjadi minimum

# 3. Total bobot MST yang dihasilkan adalah 6

# 4. Edge tertentu tidak dipilih karena dapat
#    membentuk cycle atau sudah ada jalur lain
#    yang lebih efisien


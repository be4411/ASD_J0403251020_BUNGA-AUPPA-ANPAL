#=====================================
# Nama  : Bunga Auppa Anpal
# NIM   : J0403251020
# Kelas : TPL/B2
# Praktikum 13 - Graph III: Spanning Tree
#=========================================

# ==========================================================
# DATA EDGE JARINGAN KOMPUTER
# ==========================================================

# Format data:
# (bobot, titik_awal, titik_tujuan)

edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# ==========================================================
# SORTING EDGE
# ==========================================================

# Mengurutkan edge dari bobot terkecil ke terbesar
edges.sort()

# List untuk menyimpan hasil MST
mst = []

# Variabel untuk menyimpan total bobot minimum
total_weight = 0

# Menyimpan router yang sudah terhubung
connected = set()

# ==========================================================
# PROSES KRUSKAL
# ==========================================================

# Membaca edge satu per satu
for weight, u, v in edges:

    # Jika salah satu router belum terhubung
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total
        total_weight += weight

        # Menandai router sudah terhubung
        connected.add(u)
        connected.add(v)

# ==========================================================
# OUTPUT
# ==========================================================

print("=== MST JARINGAN KOMPUTER ===")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot minimum
print("Total bobot minimum =", total_weight)

# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Kasus yang dipilih adalah Kasus 2 - Jaringan Komputer.

# 2. Algoritma yang digunakan adalah Kruskal.

# 3. Edge yang dipilih dalam MST:
#    - RouterC - RouterD (bobot 1)
#    - RouterA - RouterC (bobot 2)
#    - RouterA - RouterB (bobot 3)

# 4. Total bobot MST adalah 6.

# 5. Edge yang tidak dipilih:
#    - RouterB - RouterC (bobot 4) → membentuk siklus
#    - RouterB - RouterD (bobot 5) → membentuk siklus
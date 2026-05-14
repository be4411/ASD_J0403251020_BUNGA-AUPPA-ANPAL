#=====================================
# Nama  : Bunga Auppa Anpal
# NIM   : J0403251020
# Kelas : TPL/B2
# Praktikum 13 - Graph III: Spanning Tree
#=========================================
#=====================================
# Nama  : Bunga Auppa Anpal
# NIM   : J0403251020
# Kelas : TPL/B2
# Praktikum 13 - Graph III: Spanning Tree
#=========================================

# ==========================================================
# DATA EDGE GEDUNG
# ==========================================================

edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# ==========================================================
# PROSES KRUSKAL 
# ==========================================================

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

# Menyimpan gedung yang sudah terhubung
connected = []

for weight, u, v in edges:

    # Jika kedua gedung belum sama-sama terhubung
    if not (u in connected and v in connected):

        mst.append((u, v, weight))
        total_weight += weight

        # Menambahkan gedung ke daftar connected
        if u not in connected:
            connected.append(u)

        if v not in connected:
            connected.append(v)

# ==========================================================
# OUTPUT
# ==========================================================

print("=== MST JARINGAN GEDUNG ===")

for u, v, w in mst:
    print(u, "-", v, "=", w)

print("Total biaya minimum =", total_weight)

# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Algoritma yang digunakan adalah Kruskal

# 2. Edge yang dipilih:
#    - GedungC - GedungD
#    - GedungA - GedungC
#    - GedungB - GedungD

# 3. Total biaya minimum adalah 6

# 4. MST cocok digunakan karena dapat menghubungkan
#    seluruh gedung dengan biaya minimum tanpa cycle
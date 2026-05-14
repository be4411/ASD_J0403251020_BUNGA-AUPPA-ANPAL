#=====================================
# Nama  : Bunga Auppa Anpal
# NIM   : J0403251020
# Kelas : TPL/B2
# Praktikum 13 - Graph III: Spanning Tree
#=========================================

import heapq

# ==========================================================
# REPRESENTASI GRAPH
# ==========================================================

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# ==========================================================
# FUNGSI ALGORITMA PRIM
# ==========================================================

def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue edge
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []

    total_weight = 0

    # ======================================================
    # PROSES PRIM
    # ======================================================

    while edges:

        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))

            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# ==========================================================
# MENJALANKAN PROGRAM
# ==========================================================

mst, total = prim(graph, 'A')

print("=== MINIMUM SPANNING TREE ===")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Node awal yang digunakan adalah A

# 2. Edge pertama yang dipilih adalah A-C
#    karena memiliki bobot terkecil dari node A

# 3. Prim menentukan edge berikutnya dengan memilih
#    edge minimum dari node yang sudah dikunjungi

# 4. Total bobot MST yang dihasilkan adalah 6

# 5. Perbedaan Prim dan Kruskal:
#    - Prim fokus membangun tree dari node awal
#    - Kruskal memilih edge global terkecil
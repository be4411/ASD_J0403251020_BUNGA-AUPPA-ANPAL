#===============================================================
# Nama    : Bunga Auppa Anpal
# NIM     : J0403251020
# Kelas   : TPL-B2
#===============================================================

#===============================================================
#Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
#===============================================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)


# ......................................
# Pertanyaan Analisis:
#
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
#    DFS menggunakan pendekatan rekursif (atau stack) setiap kali
#    menemukan tetangga yang belum dikunjungi, DFS langsung masuk
#    ke rekursi lebih dalam tanpa menunggu tetangga lain di level yang sama.
#    ini menyebabkan DFS selalu menelusuri satu jalur sampai ujung 
#    sebelum balik lagi dan mencoba jalur lain
#
# 2. Apa yang terjadi jika urutan neighbor diubah?
#    Jika urutan neighbor diubah, misalnya 'A': ['C', 'B'] bukan ['B','C'],
#    maka DFS akan menelusuri cabang C terlebih dahulu (A -> C -> F),
#    baru kemudian cabang B (B -> D, B -> E). Jalur yang dieksplorasi
#    berbeda, tetapi semua node tetap akan dikunjungi (hanya urutannya
#    yang berubah)
#
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama:
#    - DFS dari A: A B D E C F  (masuk sedalam mungkin di tiap cabang)
#    - BFS dari A: A B C D E F  (kunjungi semua node per level/jarak)
#
#    DFS cocok untuk eksplorasi jalur lengkap, deteksi siklus, atau
#    mencari satu solusi yang mungkin. BFS lebih cocok untuk mencari
#    jalur terpendek karena menjamin node ditemukan berdasarkan jarak
#    minimum dari titik awal.
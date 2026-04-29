#===============================================================
# Nama    : Bunga Auppa Anpal
# NIM     : J0403251020
# Kelas   : TPL-B2
#===============================================================

#===============================================================
#Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
#===============================================================


from collections import deque

graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

# ......................................
# Pertanyaan Analisis:
#
# 1. Node mana yang dikunjungi pertama?
#    Node 'Rumah' dikunjungi pertama karena merupakan titik startnya
#    setelah itu, BFS mengunjungi semua tetangga langsung Rumah terlebih
#    dahulu, yaitu 'Sekolah' dan 'Toko' (level 1), sebelum lanjut ke
#    'Perpustakaan' dan 'Pasar' (level 2)
#
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
#    BFS menjelajahi graph secara berlapis (level by level), ini membuat
#    node yang ditemukan pertama kali adalah node yang dapat dicapai
#    dengan jumlah edge nya paling sedikit dari titik awal.
#    sehingga jalur yang ditemukan BFS selalu merupakan jalur terpendek
#    dalam graph tak bervalue
#
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
#    Jika urutan tetangga dalam graph diubah (misalnya 'Rumah' mengarah ke
#    ['Toko', 'Sekolah'] bukan ['Sekolah', 'Toko']), maka urutan kunjungan
#    pada level yang sama akan berubah (Toko dikunjungi sebelum Sekolah).
#    kalau ada edge baru ditambahkan, BFS mungkin menemukan jalur baru atau
#    node baru lebih awal, tapi prinsip level by level tetap sama
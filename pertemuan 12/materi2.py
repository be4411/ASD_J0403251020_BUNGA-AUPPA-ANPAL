#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
# Implementasi Bellman Ford pada Phyton. 
#===========================================================



def bellman_ford(graph, start):
    # Inisialisasi jarak ke semua node sebagai tak terhingga (infinity)
    distances = {node: float('inf') for node in graph}
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Relaksasi berulang sebanyak (jumlah node - 1) kali
    # Ini adalah langkah inti dari algoritma Bellman-Ford
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke 'node' sudah diketahui (bukan inf)
                # dan ditemukan jalur yang lebih murah/pendek ke 'neighbor'
                if distances[node] + weight < distances[neighbor]:
                    # Update jarak ke neighbor
                    distances[neighbor] = distances[node] + weight

    # Opsional: Cek siklus negatif (jika setelah V-1 relaksasi masih bisa update, 
    # berarti ada siklus negatif). Untuk kasus ini kita asumsikan graph aman.
    
    return distances

# Representasi graph dari ilustrasi di modul:
# A -> B bobot 5
# A -> C bobot 4
# C -> B bobot -2 (bobot negatif)
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

# Menentukan node awal
node_awal = 'A'

# Menjalankan algoritma
hasil_jarak = bellman_ford(graph, node_awal)

# Menampilkan output
print(f"Jarak terpendek dari {node_awal} menggunakan Bellman-Ford:")
for node, jarak in hasil_jarak.items():
    print(f"Jalur {node_awal} ke {node} = {jarak}")

# Penjelasan singkat kenapa Bellman-Ford hebat:
# Berbeda dengan Dijkstra, Bellman-Ford bisa menangani bobot negatif.
# Seperti kasus di atas: Jalur A -> C -> B (4 + (-2) = 2) lebih pendek
# daripada jalur langsung A -> B (5).
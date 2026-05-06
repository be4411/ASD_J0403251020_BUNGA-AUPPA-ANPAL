#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 5 : Studi Kasus dengan Program Shortest Path  
# ==========================================================

import heapq

def dijkstra(graph, start):
    
    distances = {node: float('infinity') for node in graph}
    # Jarak ke node awal adalah 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan (jarak, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Ambil node dengan jarak terkecil dari queue
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak di queue lebih besar dari jarak yang sudah tercatat, abaikan
        if current_distance > distances[current_node]:
            continue
            
        # Periksa neighbor dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jalur yang lebih pendek ke neighbor, perbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

graph_kota = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

node_awal = 'Bogor'

hasil_jarak = dijkstra(graph_kota, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil_jarak.items():
    print(f"{node_awal} -> {kota} = {jarak}")

# ==========================================================
# Jawaban Analisis:
# 1.Node awal yang digunakan apa?
# Node awal yang digunakan adalah 'Bogor'
#
# 2.Node mana yang memiliki jarak paling kecil dari node awal?
# Node 'Bogor' itu sendiri (jarak = 0), namun jika node tujuan lain, maka 'Depok' (jarak = 2)
#
# 3.Node mana yang memiliki jarak paling besar dari node awal?
# Node 'Bandung' dengan total jarak 8 (Bogor -> Depok -> Bandung)
#
# 4.Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat:
# Algoritma dimulai dari Bogor (jarak 0) melihat tetangga Bogor, yaitu Depok (2) 
# dan Jakarta (5) dijkstra memilih Depok karena lebih dekat. Dari Depok, diperbarui jarak ke Jakarta menjadi 4 (2+2) karena lebih kecil dari jalur langsung (5). 
# Terakhir, dihitung jarak ke Bandung melalui Depok (2+6=8) 
# dan melalui Jakarta (4+7=11), lalu memilih jarak terkecil yaitu 8

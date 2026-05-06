#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ==========================================================


import heapq 
# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
    'Perpustakaan': {'Lab': 3}, 
    'Kantin': {'Lab': 4, 'Aula': 7}, 
    'Lab': {'Aula': 1}, 
    'Aula': {} 
} 
def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 

    priority_queue = [(0, start)] 

    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
        if current_distance > distances[current_node]: 
            continue 
    
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight 

        if distance < distances[neighbor]: 
            distances[neighbor] = distance 
            heapq.heappush(priority_queue, (distance, neighbor)) 

    return distances 
hasil = dijkstra(graph, 'Gerbang') 
print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
 print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis: 
# 1. Lokasi mana yang paling dekat dari Gerbang? 
# Lokasi yang paling dekat adalah Kantin dengan waktu tempuh hanya 2 menit

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 
# Waktu tempuh terpendeknya adalah 7 menit. Jalur yang diambil adalah Gerbang -> Kantin -> Lab -> Aula

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
# Sebagai contoh, jalur dari Kantin ke Aula jika langsung memakan waktu 7 menit
# Tapi, jika memutar lewat Lab (Kantin -> Lab -> Aula), waktunya hanya 5 menit, Jalur memutar bisa lebih cepat jika bobot pada setiap cabangnya jauh lebih kecil daripada satu jalur langsung yang berbobot besar

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Dijkstra sangat cocok karena waktu tempuh antar lokasi di kampus tidak mungkin bernilai negatif
# Karena semua bobotnya positif, Dijkstra dapat menemukan rute paling efisien dengan sangat cepat dibandingkan algoritma lain seperti Bellman-Ford
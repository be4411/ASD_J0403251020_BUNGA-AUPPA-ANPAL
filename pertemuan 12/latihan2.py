#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 2: Implementasi Dijkstra 
# ==========================================================

import heapq 
# Weighted graph dengan bobot positif 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 
def dijkstra(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    """ 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)]

    while priority_queue: 
            current_distance, current_node = heapq.heappop(priority_queue) 
    
            # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
            # maka proses dilewati 
            if current_distance > distances[current_node]: 
                continue 
    
            # Periksa semua tetangga dari node saat ini 
            for neighbor, weight in graph[current_node].items(): 
                distance = current_distance + weight 
    
                # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
                if distance < distances[neighbor]: 
                    distances[neighbor] = distance 
                    heapq.heappush(priority_queue, (distance, neighbor)) 
    
    return distances 
    
    
hasil = dijkstra(graph, 'A') 
    
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
 print(node, "=", distance) 
 

# ==========================================================
# Jawaban Analisis: 
# 1. Berapa jarak terpendek dari A ke B? 
# Jaraknya adalah 4 karena jalur langsung A -> B memiliki bobot 4 dan tidak ada jalur alternatif lain yang lebih murah untuk mencapai B.

# 2. Berapa jarak terpendek dari A ke C? 
# Jaraknya adalah 2 didapat langsung dari edge A -> C

# 3. Berapa jarak terpendek dari A ke D? 
# Jaraknya adalah 3 ini didapat melalui rute A -> C -> D 


# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# Karena akumulasi bobot pada jalur A -> C -> D (3) lebih kecil daripada jalur A -> B -> D (9)
# Meskipun secara jumlah edge keduanya sama-sama melewati dua titik, nilai bobot pada jalur C jauh lebih efisien.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# Fungsinya adalah untuk memastikan bahwa algoritma selalu memproses node dengan jarak kumulatif terkecil terlebih dahulu.
# Ini membuat algoritma menjadi greedy yang efisien, karena tidak perlu mengecek semua kemungkinan secara acak jadi cuma fokus pada jalur yang paling memungkinkan

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Dijkstra bekerja dengan asumsi bahwa sekali sebuah node ditandai sebagai jarak terpendek, jarak tersebut tidak akan berkurang lagi
# Jika ada bobot negatif, asumsi ini rusak karena jalur yang sudah dianggap terpendek bisa saja menjadi lebih pendek lagi jika melewati edge negatif tersebut nantinya, yang dapat menyebabkan perhitungan salah atau bahkan menyebabkan infinite loop pada tipe graph tertentu
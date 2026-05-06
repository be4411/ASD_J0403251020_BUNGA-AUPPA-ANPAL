# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 
 
# Weighted graph dengan bobot negatif 
graph = { 
    'A': {'B': 5, 'C': 4}, 
    'B': {}, 
    'C': {'B': -2} 
} 
 
def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
 
        # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 
 
 
hasil = bellman_ford(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)


# Jawaban Analisis: 
# 1. Berapa bobot langsung dari A ke B? 
# Bobot langsung dari A ke B adalah 5.

# 2. Berapa total bobot jalur A -> C -> B? 
# Total bobotnya adalah 2 didapat dari bobot A ke C yaitu 4, ditambah bobot C ke B yaitu -2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? 
# Jalur yang menghasilkan jarak lebih kecil adalah jalur memutar A -> C -> B dengan total bobot 2, dibandingkan jalur langsung yang bobotnya 5

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
# Karena Bellman-Ford tidak bersifat sekali jadi seperti Dijkstra
# jadi Bellman-Ford melakukan pengecekan ulang (relaksasi) ke seluruh edge berkali-kali supaya memungkinkan algoritma untuk memperbarui jarak jika ditemukan jalur yang lebih murah akibat adanya bobot negatif, tanpa mengasumsikan bahwa jarak yang sudah ditemukan pertama kali adalah yang paling pendek. 

# 5. Apa yang dimaksud dengan proses relaksasi edge? 
# Relaksasi edge adalah proses memperbarui estimasi jarak terpendek ke suatu node. Caranya dengan membandingkan jarak yang sudah tercatat sebelumnya dengan jarak baru yang melewati sebuah node perantara
# Kalau jalur baru tersebut lebih kecil, maka nilai jarak pada node tujuan akan diperbarui.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Bobot Negatif: Bellman-Ford sanggup menangani bobot negatif dan mendeteksi negative cycle, sedangkan Dijkstra akan gagal atau salah hitung

#Kecepatan (Kompleksitas): Dijkstra jauh lebih cepat karena menggunakan priority queue, sementara Bellman-Ford lebih lambat karena harus mengulang proses relaksasi untuk semua edge sebanyak jumlah node dikurangi satu

#Cara Kerja: Dijkstra adalah algoritma greedy (memilih yang terbaik di setiap langkah), sedangkan Bellman-Ford menggunakan pendekatan dynamic programming sederhana dengan iterasi berulang
#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#===========================================================
# Implementasi DFS pada graph
#===========================================================

#representasi graph
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
  
}

# graph : dictionary yang menyimpan graph
# node : menyimpan node yang sedang dikunjungi
# visited : menyimpan node yang sudah dikunjungi

def dfs(graph, node, visited):
    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    # Tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # Lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

# Inisialisasi set untuk menyimpan node yang dikunjungi
visited = set()

# Menjalankan dfs dari A
dfs(graph, "A", visited)
#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang (nested dictionary)
# Key luar adalah simpul asal, key dalam adalah simpul tujuan, dan value adalah bobotnya
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

# Mengakses bobot antar simpul dan menjumlahkannya untuk menghitung total bobot jalur
# Menghitung jalur 1: Melewati simpul A ke B, lalu B ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # Jalur: A -> B -> D 

# Menghitung jalur 2: Melewati simpul A ke C, lalu C ke D
jalur_2 = graph['A']['C'] + graph['C']['D'] # Jalur: A -> C -> D

# Menampilkan hasil perhitungan ke layar
print("Jalur 1: A -> B -> D =", jalur_1)  
print("Jalur 2: A -> C -> D =", jalur_2)  

# Logika penentuan jalur terpendek berdasarkan nilai akumulasi bobot terkecil
if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")


# ==========================================================
# Jawaban Analisis: 
# 1. Berapa total bobot jalur A -> B -> D? 
# Total bobotnya adalah 9 didapat dari bobot A ke B sebesar 4 ditambah bobot B ke D sebesar 5

# 2. Berapa total bobot jalur A -> C -> D? 
# Total bobotnya adalah 3 didapat dari bobot A ke C sebesar 2 ditambah bobot C ke D sebesar 1


# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# Jalur yang dipilih adalah jalur A -> C -> D karena memiliki total bobot paling kecil yaitu 3


# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang apaling sedikit? 
# karena pada Weighted Graph, setiap edge punya bobot yang berbeda, seperti : jarak, waktu, atau biaya 
# Jalur dengan sedikit edge bisa saja memiliki bobot individu yang sangat besar, sehingga total akumulasinya lebih tinggi dibandingkan jalur memutar yang memiliki banyak edge tetapi bobot masing-masing edgenya kecil
  
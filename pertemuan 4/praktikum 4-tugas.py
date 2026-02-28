#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================




class Node:
    def __init__(self, plat, nama, servis):
        self.plat = plat # menyimpan nomor plat kendaraan
        self.nama = nama # menyimpan nama pemilik kendaraan
        self.servis = servis # menyimpan jenis layanan/servis
        self.next = None # pointer/penghubung ke node berikutnya 

class QueueBengkel:
    def __init__(self):
        # inisialisasi antrian baru: depan (front) dan belakang (rear) masih kosong
        self.front = None
        self.rear = None

    def is_empty(self):
        # mengecek apakah antrian kosong 
        return self.front is None
    
    # menambahkan data baru ke bagian belakang (rear)
    def enqueue(self, plat, nama, servis):
        node_baru = Node(plat, nama, servis) # membuat objek node baru

        # kalau antrian kosong, maka node baru menjadi front sekaligus rear
        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
        else:
            # kalau sudah ada isi, hubungkan node terakhir (rear) ke node baru
            self.rear.next = node_baru
            # pindahkan status 'rear' ke node yang baru masuk
            self.rear = node_baru

    # menghapus/melayani data dari bagian paling depan (front)
    def dequeue(self):
        # mengecek apakah ada orang yang bisa dilayani
        if self.is_empty():
            print("Antrian kosong! Tidak ada pelanggan yang dilayani.")
            return None
        # menyimpan data yang di front ke variabel sementara untuk ditampilkan nanti
        pelanggan_dilayani = self.front
        # menggeser pointer front ke node berikutnya (maju satu langkah)
        self.front = self.front.next
        # Kalau setelah digeser front jadi kosong, rear juga harus direset ke None
        if self.front is None:
            self.rear = None
            
        return pelanggan_dilayani
    # menampilkan seluruh isi antrian dari depan ke belakang
    def tampilkan(self):
        if self.is_empty():
            print("Antrian saat ini kosong.")
            return
      # mulai menelusuri dari data paling depan
        current = self.front
        no = 1
        print("\n--- Daftar Antrian Bengkel ---")
        while current is not None: 
            print(f"{no}. [{current.plat}] {current.nama} - Servis: {current.servis}")
            current = current.next # pindah ke node selanjutnya
            no += 1
        print("------------------------------")

def main():
    q = QueueBengkel()

    while True:
        print("\n===== Sistem Antrian Bengkel Motor =====")
        print("1. Tambah Antrian (Enqueue)")
        print("2. Layani Pelanggan (Dequeue)")
        print("3. Lihat Daftar Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            # Mengambil input dari pengguna
            plat = input("Masukkan Nomor Plat : ").strip()
            nama = input("Masukkan Nama Pemilik : ").strip()
            servis = input("Masukkan Jenis Servis : ").strip()
            q.enqueue(plat, nama, servis) # Memasukkan ke antrian
            print("Pelanggan berhasil ditambahkan ke antrian.")

        elif pilihan == "2":
            dilayani = q.dequeue() # Mengambil data terdepan
            if dilayani:
                # Menampilkan data yang baru saja dihapus/dilayani
                print(f"Melayani pelanggan: {dilayani.nama} ({dilayani.plat})")

        elif pilihan == "3": # Memanggil fungsi tampilkan
            q.tampilkan()

        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break # Menghentikan perulangan
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            
# Menjalankan program utama
if __name__ == "__main__":
    main()
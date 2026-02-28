#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#==========================================================
#Studi Kasus : Sistem Antrian Layanan Akademik 
#Implementasi Queue =>
# Stack => Front c-> B-> A -> none 
# Enqueue : memindahkan pointer rear (nambah data dari belakang)
# Dequeue : memindahkan pointer front (menghapus data dari depan)
# Front -> A -> B -> C -> Rear
#==========================================================

#1) mendefinisikan node (unit dasar linked list)

class Node:
    def __init__(self,nim,nama):
        self.nim = nim #menyimpan nim mahasiswa
        self.nama = nama #menyimpan nama mahasiswa
        self.next = None #pointer ke node berikutnya

#2) mendfinisikan queue, terdiri dari front dan rear
class queueAkademik :
    def __init__(self):
        self.front =None
        self.rear = None
    def is_empty(self):
        #ketika queue kosong maka front = rear = none
        return self.front is None
    
    #menambahkan data baru ke bagian belakang (rear)
    def enqueue(self,nim,nama):
        Nodebaru = Node(nim,nama)
        #jika data baru masuk dari queue yang kosong maka data baru = front -> rear
        if self.is_empty():
            self.front = Nodebaru
            self.rear = Nodebaru
            return
        #jika queue tidak kosng, maka data baru diletakan setelh rear kemudian dijadikan sebagai rear
        
        self.rear.next = Nodebaru
        self.rear = Nodebaru

#menghapus data paling depan(memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print("antrian kosong. tidak ada mahasiswa yang dilayani")
        #lihat data bagian front, simpan di variabel datayang dihapus (dilayani)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None :
            self.rear = None
        return node_dilayani

    def tampilkan(self):
        current = self.front
        no = 1
        while current is not None :
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#program Utama

def main():
    #instantisasi queue
    q = queueAkademik()

    while True :
        print("=====Sistem antrian akademik====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. keluar")

        pilihan = input("pilih menu (1-4):").strip()

        if pilihan == "1":
            nim =  input("masukan nim : ").strip()
            nama = input("masukan nama : ").strip()
            q.enqueue(nim,nama)
            print("mahasiswa berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani:
                print(f"Mahasiswa dilayani: {dilayani.nim} - {dilayani.nama}")
            else:
                print("Antrian kosong. Tidak ada mahasiswa yang dilayani.")
        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("program selesai")
            break
        else :
            print("pilihan tidak valid, silahkan pilih menu 1-4")

        
#menjalankan program
if __name__ == "__main__":
    main()
#================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#================================================

#================================================
#Implementasi Dasar : Node pada Linked List
#================================================

#Membuat class Node (merupakan unit dasar)
class Node: #class implementasi stack
    def __init__(self, data): #konstruktor
        self.data = data #menyimpan nilai data
        self.next = None #pointer ke note berikutnya

#Proses 1
NodeA = Node("A") #proses memanggil konstruktor dalam class node
NodeB = Node("B")
NodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
NodeA.next = NodeB
NodeB.next = NodeC

# 3) Menentukan node pertama (head)
head = NodeA

# 4) Traversal : menelusuri dari head samapi none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

#================================================
#Implementasi Dasar : Linked List + Insert Awal
#================================================

class LinkedList :
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self, data): #push d
        #1) buat node baru
        nodeBaru = Node(data) #panggil class node

        #2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        #3) head pindah ke node baru
        self.next = nodeBaru

    def hapus_awal(self):#pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang di hapus adalah : " , data_terhapus)
        
    def tampilkan(self): #implementasi traversal
        current = self.head
        while current is not None :
            print(current.data)
            current = current.next
print("=======list baru =========")
ll = LinkedList() #instantiasi objek ke clas linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()

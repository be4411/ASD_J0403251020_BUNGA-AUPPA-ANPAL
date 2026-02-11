class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularsinglyLinkedlist :
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self,data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
             self.tail.next = new_node
             self.tail = new_node
             self.tail.next = self.head
    
    def search(Self, key):
        if not Self.head :
            return None
        
        temp = Self.head
        while True :
            if temp.data == key :
                return True
            temp = temp.next
            if temp == Self.head :
                break

        return False

cll = CircularsinglyLinkedlist()

data_input = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

print("Masukkan elemen ke dalam Circular Linked List:",
      data_input if data_input.strip() else "(Tidak ada elemen)")

if data_input.strip():
    for num in map(int, data_input.split(",")):
        cll.insert_at_end(num)

key = int(input("Masukkan elemen yang ingin dicari: "))

if not cll.head:
    print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
elif cll.search(key):
    print(f"Elemen {key} ditemukan dalam Circular Linked List.")
else:
    print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")



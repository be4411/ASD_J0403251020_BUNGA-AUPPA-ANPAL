class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if not self.head:
            return "kosong"

        result = ""
        temp = self.head
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        return result + "null"

    def merge(self, other):
        if not self.head:
            return other
        if not other.head:
            return self

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head
        return self

ll1 = LinkedList()
ll2 = LinkedList()

# Input 1
data1 = input("Masukkan elemen untuk Linked List 1: ")
if data1.strip():
    for num in map(int, data1.split(",")):
        ll1.insert_at_end(num)

# Input 2
data2 = input("Masukkan elemen untuk Linked List 2: ")
if data2.strip():
    for num in map(int, data2.split(",")):
        ll2.insert_at_end(num)

# Tampilkan List
print("\nLinked List 1:", ll1.display())
print("Linked List 2:", ll2.display())

# Gabungkan
merged = ll1.merge(ll2)

print("Linked List setelah digabungkan:", merged.display())

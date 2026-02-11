class node :
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data) :
        new_node = node(data)
        if not self.head :
            self.head = new_node
            return
        temp = self.head 
        while temp.next :
            temp = temp.next
        temp.next = new_node

    def delete_node(self,key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key :
            prev = temp
            temp = temp.next
        if temp is None:
            print("Data tidak ditemukan")
            return
        prev.next = temp.next
        temp = None
        
    def display(Self):
        temp = Self.head
        while temp:
            print(temp.data,  end=" ->")
            temp = temp.next
        print("null")

ll = Linkedlist()
ll.insert_at_end(3)
ll.insert_at_end(7)
ll.insert_at_end(12)
ll.insert_at_end(19)

ll.display()
ll.delete_node(12)
ll.display() 
        
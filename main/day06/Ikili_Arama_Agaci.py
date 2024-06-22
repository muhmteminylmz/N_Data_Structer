#dugum olusturma sinifi ve kurucu metodlar

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

#kuyruk sinifi
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    def __str__(self):
        values = (str(x) for x in self.linkedList)
        return "".join(values)
    #kuyruga ekleme methodu
    def enqueue(self,value):
        new_node = Node(value)
        if self.linkedList.head == None:
           self.linkedList.head = new_node
           self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    #kuyrugun bos olup olmadiginin kontrolu
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    #Kuyruktan kaldirma metodu
    def dequeue(self):
        if self.isEmpty():
            return "Kuyruk Bos"
        else:
            tempNode = self.linkedList.head
        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head == None
            self.linkedList.tail = None
        else:
            self.linkedList.head = self.linkedList.head.next
        return tempNode

    #mevcut degeri ognrenme methodu
    def peek(self):
        if self.isEmpty():
            return "Buyruk Bos"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

class Queue:
    def __init__(self):
        self.items = []
        print('Kuyruk olusturuldu.')
    def __str__(self): #print gibi fonksiyonlarda cagrilir
        elemanlar=[str(x) for x in self.items]
        return '\n'.join(elemanlar)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self,deger):
        self.items.append(deger)
        print('eleman kuyruga eklendi')
    def dequeue(self):
        if self.isEmpty():
            print('Kuyruk bos')
        else:
            return self.items.pop(0)
    def peek(self):
        if self.isEmpty():
            print('Kuyruk bos')
        else:
            return self.items[0]


kuyruk = Queue()
print(kuyruk.isEmpty())
print(kuyruk)

kuyruk.enqueue(5)
kuyruk.enqueue(15)
kuyruk.enqueue(25)
print(kuyruk)
print()

print(kuyruk.peek())
print()

kuyruk.dequeue()
print(kuyruk)
print()

""" 
Kuyruk olusturuldu.
True

eleman kuyruga eklendi
eleman kuyruga eklendi
eleman kuyruga eklendi
5
15
25

5

15
25
"""
#Yiginda genelde LIFO(last in first out) kullanilir
class Stack:
    def __init__(self,boyut): #self: burdaki elemanlara disardan erisim saglayabilmek icin
        self.list = []
        self.boyut = boyut
        print("Stack initialised")
    def __str__(self):
        deger=self.list.reverse() #liste mantigiyla ilk elemana erisebilmek icin
        deger=[str(x) for x in self.list]
        return '\n'.join(deger)
    def isFull(self):
        if len(self.list) == self.boyut:
            return True
        else:
            return False

    def push(self,eleman):
        if self.isFull():
            print("Yigin dolu")
        else:
            self.list.append(eleman)
            print("Eleman yigina eklendi.")

yigin=Stack(3) #uzunluk (index degil)
yigin.push(3)
yigin.push('ali')
yigin.push('Mehmet')
yigin.push('mustafa')
yigin.push('Ahmet')
print()

print(yigin)
print(yigin)


""" 
Stack initialised
Eleman yigina eklendi.
Eleman yigina eklendi.
Eleman yigina eklendi.
Yigin dolu
Yigin dolu

Mehmet
ali
3
"""
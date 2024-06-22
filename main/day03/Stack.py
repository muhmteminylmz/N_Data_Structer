#Yiginda genelde LIFO(last in first out) kullanilir
class Stack:
    def __init__(self): #self: burdaki elemanlara disardan erisim saglayabilmek icin
        self.list = []
        print("Stack initialised")

    def __str__(self):
        deger=self.list.reverse() #liste mantigiyla ilk elemana erisebilmek icin
        deger=[str(x) for x in self.list]
        return '\n'.join(deger)
    def isEmpty(self):
        return len(self.list)==0

    def push(self,x):
        self.list.append(x)
        print("Eleman yigina eklendi")

    def pop(self):#son elemani siler(sadece sona erisimimiz var)
        if self.isEmpty():
            print("Yigin bos")
        else:
            self.list.reverse()
            print("Eleman yigindan silindi")
            return self.list.pop() #(yigindan bagimsiz)listenin son elemanini silmek icin normalde pop kullanilir

    def peek(self):#son elemani silmeden gosterir
        if self.isEmpty():
            print("Stack bos")
        else:
            self.list.reverse()
            return self.list[len(self.list)-1]

    def delete(self):#tum yapiyi silmek icin
        print("Yigin silindi.")
        self.list=None

yigin=Stack()
print(yigin.isEmpty())

yigin.push(16)
yigin.push(21)
yigin.push(72)
yigin.push('Ali')

print(yigin)
print()

yigin.pop() #en son eklenen elemana erisebildigimiz icin onu siler

print(yigin)
print()

print('peek metodu ile ogrenilen deger: ',yigin.peek())
print()

yigin.delete()
#print(yigin) yigin komple silindiginden yazdiramiyoruz

""" 
Stack initialised
True
Eleman yigina eklendi
Eleman yigina eklendi
Eleman yigina eklendi
Eleman yigina eklendi
Ali
72
21
16

Eleman yigindan silindi
72
21
16

peek metodu ile ogrenilen deger:  72

Yigin silindi.

"""
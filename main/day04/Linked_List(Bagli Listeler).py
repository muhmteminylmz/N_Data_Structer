class Node:
    def __init__(self, veri=None):
        self.veri = veri
        self.sonraki = None


class SLinked_List:
    def __init__(self):
        self.ilkdugum = None

    def liste_yaz(self):
        dugum = self.ilkdugum
        while dugum is not None:
            print(dugum.veri)
            print(dugum.sonraki)
            dugum = dugum.sonraki

    def basa_ekle(self, yeni_veri):
        yenidugum = Node(yeni_veri)
        yenidugum.sonraki = self.ilkdugum
        self.ilkdugum = yenidugum

    def sona_ekle(self, yeniveri):
        yenidugum = Node(yeniveri)
        if self.ilkdugum is None:
            self.ilkdugum = yenidugum
            return
        ilk = self.ilkdugum
        while (ilk.sonraki): #eger bos veya none degilse true kabul edilir
            ilk = ilk.sonraki
        ilk.sonraki = yenidugum

    def sil(self, dugum):
        ilkdugum = self.ilkdugum
        if (ilkdugum is not None):
            if (ilkdugum.veri == dugum):
                self.ilkdugum = ilkdugum.sonraki()
                ilkdugum = None
                return
            while (ilkdugum is not None):
                if (ilkdugum.veri == dugum):
                    break
                prev = ilkdugum
                ilkdugum = ilkdugum.sonraki
            if (ilkdugum == None):
                return
            prev.sonraki = ilkdugum.sonraki
            ilkdugum = None


liste = SLinked_List()
d1 = Node("Kirmizi")
d2 = Node("Yesil")
d3 = Node("Siyah")
d4 = Node("Mavi")
liste.ilkdugum = d1
d1.sonraki = d2
d2.sonraki = d3
d3.sonraki = d4
liste.basa_ekle("Mor")
liste.sona_ekle("Pembe")
liste.liste_yaz()

print("#####################################")
# ------------------------------------------------------------------------------------------

liste2 = SLinked_List()
d5 = Node("Kirmizi")
d6 = Node("Yesil")
d7 = Node("Siyah")
d8 = Node("Mavi")
liste2.ilkdugum = d5
d5.sonraki = d6
d6.sonraki = d7
d7.sonraki = d8
liste2.basa_ekle("Mor")
liste2.sona_ekle("Pembe")
liste2.liste_yaz()
liste2.sil("Mavi")
print("Maviyi silme islemi yapildi","\n")
liste2.liste_yaz()

""" 
Mor
<__main__.Node object at 0x000001AB145F7010>
Kirmizi
<__main__.Node object at 0x000001AB145F7050>
Yesil
<__main__.Node object at 0x000001AB145F7090>
Siyah
<__main__.Node object at 0x000001AB145F70D0>
Mavi
<__main__.Node object at 0x000001AB145F7250>
Pembe
None
#####################################
Mor
<__main__.Node object at 0x000001AB145F7290>
Kirmizi
<__main__.Node object at 0x000001AB145F7310>
Yesil
<__main__.Node object at 0x000001AB145F7350>
Siyah
<__main__.Node object at 0x000001AB145F7390>
Mavi
<__main__.Node object at 0x000001AB145F7410>
Pembe
None
Maviyi silme islemi yapildi 

Mor
<__main__.Node object at 0x000001AB145F7290>
Kirmizi
<__main__.Node object at 0x000001AB145F7310>
Yesil
<__main__.Node object at 0x000001AB145F7350>
Siyah
<__main__.Node object at 0x000001AB145F7410>
Pembe
None
"""
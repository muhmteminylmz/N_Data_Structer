#hiyararsik bir duzen vardir(xml,html)
#yol = dugumlerin dizisi
#yukseklik = dugumun yuksekliginden yapraga kadar olan mevcut kenar sayisi (asagiya dogru)
#derinlik = kokten dugume kadar olan kenarlarin sayisi (yukariya dogru)
#derece = Dugumun toplam dal sayisi
#Agac derinligi = Bir agacin yuksekligi ve derinligi iki esdeger tanimdir kok dugumun yuksekligi veya en uzaktaki dugumun derinligi

class TreeNode:
    def __init__(self,veri,cocuklar=[]):
        self.veri = veri
        self.cocuklar = cocuklar

    def __str__(self,seviye=0):
        sonuc=" "*seviye+str(self.veri)+"\n"
        for cocuk in self.cocuklar:
            sonuc+= cocuk.__str__(seviye+1)
        return sonuc

    def cocuk_ekle(self,TreeNode):
        self.cocuklar.append(TreeNode)

D1 = TreeNode("D1",[])
D2 = TreeNode("D2",[])
D3 = TreeNode("D3",[])
D1.cocuk_ekle(D2)
D1.cocuk_ekle(D3)

D4= TreeNode("D4",[])
D5= TreeNode("D5",[])
D6= TreeNode("D6",[])
D7 = TreeNode("D7",[])
D8= TreeNode("D8",[])

D2.cocuk_ekle(D4)
D2.cocuk_ekle(D5)

D3.cocuk_ekle(D6)
D4.cocuk_ekle(D7)
D4.cocuk_ekle(D8)

print(D1)
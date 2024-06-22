import numpy
from numpy import *
from array import *


dizi=array('i',[])
dizi.append(12)

print(dizi)

dizi.append(56)
print(dizi)

#dizi.insert(0,32)
print(dizi) 
dizi.insert(4,61)
print(dizi)
dizi.insert(15,53)
print(dizi)

dizi=array('i',[21,16,25,56,72,34,55,15])
for eleman in dizi:
  print(eleman)

for eleman in dizi:
  if eleman%10==5:
    print(eleman)

print(dizi[0])

def eleman_ara(dizi,aranilan):
  for i in range(len(dizi)):
    if dizi[i]==aranilan:
      return i
  return "eleman bulunamadi"
print(eleman_ara(dizi,4))
print(eleman_ara(dizi,15))

dizi.remove(25)
print(dizi)
dizi2=array('i',[12,13])

dizi.extend(dizi2) #baska bir dizi ekleme
print(dizi)
L=[40,45]
dizi.fromlist(L) #gene dizi ekleme
print(dizi)
dizi.index(34)
dizi.reverse()
print(dizi)

print(dizi.buffer_info())
print("Count: ")
print(dizi.count(12))

matris=numpy.array([[4,3,7],[1,4,2],[7,9,2]])
print(matris)
#normalde sadece array vardi ben numpy.array yaptim arastir
matris2=insert(matris,2,[11,12,13],axis=1)
print(matris2)

matris3=append(matris,[[11,12,13]],axis=0)
print(matris3)

def elemanlaraerisim(matris, satirno, sutunno): #eleman ariyor
  if(satirno>=len(matris) or sutunno>=len(matris[0])):
    return "hatali giris"
  else:
      return matris[satirno][sutunno]
matris=([[4,3,7,8],[1,4,8,2],[7,9,2,5],[12,17,92,22]])
print(elemanlaraerisim(matris,2,2))

for i in range(len(matris)):
  for j in range(len(matris[0])):
    if matris[i][j]%2==0:
      print(matris[i][j], end="")

def matrisde_ara(matris,aranilan):
  for i in range(len(matris)):
    for j in range(len(matris[0])):
      if matris[i][j]==aranilan:
        return "satir="+str(i)+"sutun="+str(j)
  return "eleman bulunamadi"
matris=([[4,3,7,8],[1,4,8,2],[7,9,2,5],[12,17,92,22]])
print(matrisde_ara(matris,7))
print(matrisde_ara(matris,18))

matris=([[4,3,7,8],[1,4,8,2],[7,9,2,5],[12,17,92,22]])
matris2=delete(matris,1,axis=0)
print(matris2)

bos_liste=[]
print(bos_liste)
liste_sayi=[34,21,12,16]
print(liste_sayi)
karisik_liste=[16,34.5,'pazartesi','ali']
print(karisik_liste)
iciceliste=[12,13,[72,68]]
print(iciceliste)

karisik_liste=[16,34.5,'pazartesi','ali']
print(karisik_liste[0])
print(karisik_liste[-2])

print(karisik_liste[0:2])

karisik_liste=[16,34.5,'pazartesi','ali']
print("orjinal liste:", karisik_liste)
karisik_liste[1]="mustafa"
karisik_liste[2]="sali"
print("degisikliksonrasi:",karisik_liste)
karisik_liste.insert(2, "fatma")
print(karisik_liste)

a=karisik_liste.pop(1)
print(karisik_liste)

if 'sali' in karisik_liste:
  print("eleman bulundu")
else:
  print("bulunamadi")

L1=[1,3,5,7,9]
L2=[0,2,4,6,8]

L3=L1+L2
print(L3)

L4=L2*3 #listeyi 3 kere tekrar eder
print(L4)

L3.sort()
print(L3)
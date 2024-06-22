import collections

sozluk1={'renk1':'kirmizi','renk2':'yesil'}
sozluk2={'renk3':'sari','renk4':'mavi'}

CM= collections.ChainMap(sozluk1,sozluk2)
print(CM.maps,'\n')
print("Anahtarlar={}".format(list(CM.keys())))
print("Degerler={}".format(list(CM.values())))
print("Elemanlar:")

for anahtar,deger in CM.items():
    print("{}:{}".format(anahtar,deger))
    print()

print('CM de renk2 var mi?:{}'.format("renk2" in CM))
print('CM de renk5 var mi?:{}'.format("renk5" in CM))

#yeni eleman ekleme
CM["renk5"]="siyah"
print(CM)

#eleman silme
del CM["renk2"]
print(CM)

#anahtar disindaki kelimelere ulasmak icin
# 1.kumeyi direkt parent olarak aldi ve 2.yi verdi
print(CM.parents)

""" 
[{'renk1': 'kirmizi', 'renk2': 'yesil'}, {'renk3': 'sari', 'renk4': 'mavi'}] 

Anahtarlar=['renk3', 'renk4', 'renk1', 'renk2']
Degerler=['sari', 'mavi', 'kirmizi', 'yesil']
Elemanlar:
renk3:sari

renk4:mavi

renk1:kirmizi

renk2:yesil

CM de renk2 var mi?:True
CM de renk5 var mi?:False
ChainMap({'renk1': 'kirmizi', 'renk2': 'yesil', 'renk5': 'siyah'}, {'renk3': 'sari', 'renk4': 'mavi'})
ChainMap({'renk1': 'kirmizi', 'renk5': 'siyah'}, {'renk3': 'sari', 'renk4': 'mavi'})
ChainMap({'renk3': 'sari', 'renk4': 'mavi'})
"""
S1={1:"bir",2:"iki",3:"uc",4:"dort",5:"bes"}
S2={"beyaz":"white","siyah":"black","pembe":"pink","yesil":"green","sari":"yellow"}
print(S1)
print(S2)

S3={"ad":"mustafa","soyad":"kaya","yas":10}
print(S3)

renkler = S2.copy()
print(renkler)

dersler=("a","b","c","d")
notlar=50
sozluk=dict.fromkeys(dersler,notlar)
print(sozluk)
print(renkler.get("beyaz"))
print(renkler.items()) #key ve valueleri ayri ayri donduruyor
print(renkler.keys())
print(renkler.values())
print(len(renkler))
print(sorted(renkler,reverse=True)) #anahtar degerlerin tersine gore siralar

"""
{1: 'bir', 2: 'iki', 3: 'uc', 4: 'dort', 5: 'bes'}
{'beyaz': 'white', 'siyah': 'black', 'pembe': 'pink', 'yesil': 'green', 'sari': 'yellow'}
{'ad': 'mustafa', 'soyad': 'kaya', 'yas': 10}
{'beyaz': 'white', 'siyah': 'black', 'pembe': 'pink', 'yesil': 'green', 'sari': 'yellow'}
{'a': 50, 'b': 50, 'c': 50, 'd': 50}
white
dict_items([('beyaz', 'white'), ('siyah', 'black'), ('pembe', 'pink'), ('yesil', 'green'), ('sari', 'yellow')])
dict_keys(['beyaz', 'siyah', 'pembe', 'yesil', 'sari'])
dict_values(['white', 'black', 'pink', 'green', 'yellow'])
5
['yesil', 'siyah', 'sari', 'pembe', 'beyaz']
"""
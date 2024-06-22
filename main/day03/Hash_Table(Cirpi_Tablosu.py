def h_tablo_goster(tablo):
    for i in range(len(tablo)):
        print(i,end="")
        for j in tablo[i]:
            print("-->",end="")
            print(j,end="")
        print()


tablo=[[]for _ in range(10)]

def Hashing(anahtar):
    return anahtar%len(tablo)

def ekle(tablo,anahtar,deger):
    yer=Hashing(anahtar)
    tablo[yer].append(deger)

ekle(tablo,10,'Ahmet')
ekle(tablo,25,'Mehmet')
ekle(tablo,20,'Can')
ekle(tablo,9,'mustafa')

h_tablo_goster(tablo)
print()

def modASCII(string,tablo_boyut):
    toplam=0
    for i in string:
        toplam+=ord(i)
    return toplam%tablo_boyut

print(modASCII("BABC",20))

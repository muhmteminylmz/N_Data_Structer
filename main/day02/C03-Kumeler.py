gunler=set(["ptrsi","sali","cars","pers","cuma","ctesi","pazar"])
#set kume tanimlamak icin kullaniliyor
asal_sayilar={2,3,5,7,11,13,17}
plakano={"01","02","03","04","34","72","61"}
#elemanlar karisik yazilir cunku index yok
print(gunler)
print(asal_sayilar)
print(plakano)
asal_sayilar.add(44)
print(asal_sayilar)
asal_sayilar.discard(13)
print(asal_sayilar)

K1=set([1,2,3,4,5,6])
K2=set([3,4,5,6,7,8])
K3=K1|K2 #birlestirme islemi
#K3 = K1.union(K2)
print(K3)

K4=K1&K2 #kesisim islemi
#K4=K1.intersection(K2)
print(K4)

#farkli elemanlarini yazdir
K1K2 = K1-K2
print(K1K2)

K2K1 = K2-K1
print(K2K1)

K3=set([1,2,3,4,5,6])
K4=set([3,4,5,6])

#kapsama
print(K4>K3)
print(K3>K4)

""" 
{'ptrsi', 'pazar', 'cuma', 'pers', 'sali', 'ctesi', 'cars'}
{17, 2, 3, 5, 7, 11, 13}
{'72', '61', '03', '34', '02', '01', '04'}
{17, 2, 3, 5, 7, 11, 44, 13}
{17, 2, 3, 5, 7, 11, 44}
{1, 2, 3, 4, 5, 6, 7, 8}
{3, 4, 5, 6}
{1, 2}
{8, 7}
False
True
"""
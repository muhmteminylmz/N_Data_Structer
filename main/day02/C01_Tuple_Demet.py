from array import *
dizi=array("i",[21,16,56,82,34])
print(dizi)

array('i',[21,16,56,72,34])

tuple1=()
print(tuple1)
tuple1=(10,"Hasan",7.9)
print(tuple1)

demet=()
print(demet)
demet = ("elma",[12,45,52],(14,21,34))
print(demet)

demet2=('p','y','t','h','o','n')
print(demet2[1])
print(demet2[-1])

print(demet[0][2])
print(demet[1][2])

print(demet2[1:4])
print("demet: :")
print(demet2[:])

print('t' in demet2) #demetin icinde olup olmadigini kontrol eder bool olarak dondurur
print(21 in demet[2])
print([12,45,52] in demet)

dizi=[8,10,12]
yeni = tuple(dizi)
print(type(yeni))

"""
array('i', [21, 16, 56, 82, 34])
()
(10, 'Hasan', 7.9)
()
('elma', [12, 45, 52], (14, 21, 34))
y
n
m
52
('y', 't', 'h')
demet: :
('p', 'y', 't', 'h', 'o', 'n')
True
True
True
<class 'tuple'>
"""
"""
Ust >= Alt Dugum -> max Heap
Ust <= ALT Dugum -> min Heap
heapify(): Listeden heap agaci olusturma methodu
heappush(): Tanimlanmis olan bir heap agacina eleman eklemek icin
heappop(): Tanimlanmis olan bir heap agacindan en kucuk degeri bulur ve cikarir.
heapreplace(): En kucuk elemani yeni bir degerle degistirir.
234
"""

import heapq

liste = [21, 16, 72, 56, 65, 34]
heapq.heapify(liste)
print(liste)
heapq.heappush(liste,12)
print(liste)
heapq.heappop(liste)
print(liste)
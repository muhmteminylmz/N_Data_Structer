# düğüm ve kenarların gösterilmesi
class graph:
    def __init__(self, sozluk=None):
        if sozluk is None:
            sozluk = {}
        self.sozluk = sozluk

    # düğümlerin yazdırılması
    def dugumListele(self):
        return list(self.sozluk.keys())

    # kenarların listelenmesi
    def kenarlar(self):
        return self.kenarListele()

    def kenarListele(self):
        kenarisimleri = []
        for d in self.sozluk:
            for dd in self.sozluk[d]:
                if {dd,d} not in kenarisimleri:
                    kenarisimleri.append({d,dd})
        return kenarisimleri


    def kenarEkle(self, kenar):
        kenar = set(kenar)
        (d1,d2) = tuple(kenar)
        if d1 in self.sozluk:
            self.sozluk[d1].append(d2)
        else:
            self.sozluk[d1] = d2

    def dugumEkle(self, dugum):
        if dugum not in self.sozluk:
            self.sozluk[dugum] = []

graf = {
    "A": ["A", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["B", "D"]
}
print(graf)
g = graph(graf)
print("Düğüm Listesi:", g.dugumListele())
print("Kenarlar:", g.kenarListele())

g.dugumEkle("F")
g.kenarEkle({'A', 'F'})  # A düğümü ile F düğümü arasında bağlantı oluştu
g.kenarEkle({'C', 'F'})  # C düğümü ile F düğümü arasında bağlantı oluştu

print("Düğüm Listesi:", g.dugumListele())
print("Kenarlar:", g.kenarListele())

class Graph:
    def __init__(self, sozluk=None):
        if sozluk is None:
            sozluk = {}
        self.sozluk = sozluk

    def addEdge(self, dugum, kenar):
        self.sozluk[dugum].append(kenar)

    def bfs(self, dugum):
        ziyaretEdilmis = [dugum]
        kuyruk = [dugum]
        while kuyruk:
            deDugum = kuyruk.pop(0)
            print(deDugum, end="->")
            for komsular in self.sozluk[deDugum]:
                if komsular not in ziyaretEdilmis:
                    ziyaretEdilmis.append(komsular)
                    kuyruk.append(komsular)

    def dfs(self, dugum):
        ziyaretEdilmis = [dugum]
        kuyruk = [dugum]
        while kuyruk:
            deDugum = kuyruk.pop()
            print(deDugum, end=">")
            for komsular in self.sozluk[deDugum]:
                if komsular not in ziyaretEdilmis:
                    ziyaretEdilmis.append(komsular)
                    kuyruk.append(komsular)


graf = {
    "0": {"1", "2", "3"},
    "1": {"0", "4"},
    "2": {"0", "4", "5", "6"},
    "3": {"0", "6", "7", "8"},
    "4": {"1", "2"},
    "5": {"2"},
    "6": {"2", "3", "9"},
    "7": {"3", "8"},
    "8": {"3", "7", "9"},
    "9": {"6", "8"}
}

g = Graph(graf)
g.bfs("0")
print("\n")
g = Graph(graf)
g.dfs("0")
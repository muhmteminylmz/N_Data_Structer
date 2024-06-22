#Sol,Sag,Kok
class TreeNode:
    def __init__(self,veri):
        self.veri = veri
        self.solcocuk=None
        self.sagcocuk=None
    def PostOrderDolasim(self,kok):
        if not kok:
            return
        self.PostOrderDolasim(kok.solcocuk)
        self.PostOrderDolasim(kok.sagcocuk)
        print(kok.veri, end="->")


D1 = TreeNode("D1")
D2 = TreeNode("D2")
D3 = TreeNode("D3")
D4= TreeNode("D4")
D5= TreeNode("D5")
D6= TreeNode("D6")
D7 = TreeNode("D7")
D8= TreeNode("D8")
D9= TreeNode("D9")

D1.solcocuk=D2
D1.sagcocuk=D3
D2.solcocuk=D4
D2.sagcocuk=D5
D3.solcocuk=D6
D3.sagcocuk=D7
D4.solcocuk=D8
D4.sagcocuk=D9
D1.PostOrderDolasim(D1)
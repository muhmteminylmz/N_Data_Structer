#Her dugum en fazla 2 cocugu olabilir
#Tam ikili ve Mukemmel ikili agac olarak ikiye ayrilir
#Mukemmelde tum dugumlerin derinligi ayni

#In Order -> Dugumler sol,kok,sag
#Post Order -> sol,sag,kok
#Pre Order -> Dugumler kok,sol,sag
#Bunlarin geneline Derinlik Dolasimlari(Önce Derinlik) denir

#Genislik Dolasimi

#Gorseldeki post order da D8 den sonra D9 gelir cunku 2 cocuguda tanimlamaliyiz geri donus hareketi yapamiyoruz

"""
        D1
       /  \
      D2   D3
     / \    / \
   D4  D5  D6 D7
  / \
D8   D9

PreOrder: D1-D2-D4-D8-D9-D5-D3-D6-D7
PostOder: D8-D9-D4-D5-D2-D6-D7-D3-D1
InOrder: D8-D4-D9-D2-D5-D1-D6-D3-D7
"""

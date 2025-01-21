def occ_liste(liste, char) :
    new_lst = []
    for mot in liste : 
        nb0cc = 0
        for lettre  in mot : 
            if lettre == char :
                nb0cc += 1
        new_lst.append(nb0cc)

 
ptit_dej = ['biscottes', 'chocolat', 'cafe', 'tartines', 'the']
print(occ_liste(ptit_dej, 'c')) # retournera [1, 2, 1, 0, 0]
# travaileur = [['Alice', 'Canadian', 8878],
#              ['Frank', 'Chinese', 2392],
#              ['bella ', 'Brazilian', 6983],
#              ['Charlie', 'French', 7697],
#              ['Lucy', 'Belgian', 4185]]

# somme = 0

# for salaire in range(len(travaileur)) :
#     somme += travaileur[salaire][2]
#     pourcentage = round((travaileur[salaire][2] / somme) * 100, 2)
#     print(f""" 
# x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
# x Prénom : {travaileur[salaire][0]} x
# x Nationalité : {travaileur[salaire][1]} x
# x Salaire : {travaileur[salaire][2]} x
# x Pourcentage de salaire dans le groupe : {pourcentage} x
# x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
# """)      
# # print(somme)


# matrice = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# ligne_2 = 0
# col_3 = 0

# graph = []
# somme = 0 
# for i in range(len(matrice)) : 
#     for j in range(len(matrice)) :
#         # print(matrice[i][j])
#         somme += matrice[i][j]
# print(somme)


# *************************************************************************************************************


# for ligne in range(len(matrice)) :
#     if ligne == 1 :
#         ligne_2 += sum(matrice[ligne])
# for col in range(len(matrice)) : 
#     # if col == 2 :
#     col_3 += matrice[col][2]
# for valeurs in range(len(matrice)) :
#     graph.append(matrice[valeurs])

# print(graph)
# print(f"  ligne de 2 : {ligne_2}\n  col 3 : {col_3}")

# ****************************************************************************************************************************


# matrice = [
#     [12, 15, 7],
#     [10, 25, 18],
#     [14, 3, 20]
# ]

# max_1 = 0
# max_2 = 0
# max_3 = 0

# for i in range(len(matrice)) :
#     if i == 0 :
#         max_1 = max(matrice[i])
#     elif i == 1 :
#         max_2 = max(matrice[i])
#     elif i == 2 : 
#         max_3 = max(matrice[i])
    
# print(f"{max_1},  {max_2}, {max_3}")

# *****************************************************************************************

# matrice1 = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# matrice2 = [
#     [7, 8, 9],
#     [10, 11, 12]
# ]

# somme = []

# for i in range(len(matrice1)) :
#     ligne_somme = []

#     for j in range(3) :
#         ligne_somme.append(matrice1[i][j] + matrice2[i][j])
    
#     somme.append(ligne_somme)

# print(somme)3

# *****************************************************************************
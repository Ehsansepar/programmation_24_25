students = [
    ["Alice", 14, 16, 15],  # les notes en math, physique, chimie
    ["Bob", 10, 12, 11],
    ["Charlie", 17, 14, 15]
]

# for i , student in enumerate(students):
#     print(f"Nom: {student[0]}, Math: {student[1]}, Physique{student[2]}, Chimie: {student[3]}")


meilleure_moyenne = 0
meilleure_etudiant = ""

for i in range(len(students)) : 
    somme_notes =  sum(students[i][1:4])
    moyenne =  somme_notes / 3
    print(f"Nom: {students[i][0]}, Note moyenne: {round(moyenne, 2)}")
    
    if moyenne > meilleure_moyenne :
        meilleure_moyenne = moyenne
        meilleure_etudiant = students[i][0]
        # print(f"Meilleur élève: {meilleure_etudiant}")
print()
print("Meilleur  élève: ", meilleure_etudiant, "\nla moyenne de ", round(meilleure_moyenne, 2))
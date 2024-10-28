students = [
    ["Alice", 14, 16, 15],  # les notes en math, physique, chimie
    ["Bob", 10, 12, 11],
    ["Charlie", 17, 14, 15]
]

# for i , student in enumerate(students):
#     print(f"Nom: {student[0]}, Math: {student[1]}, Physique{student[2]}, Chimie: {student[3]}")

for i in range(len(students)) : 
    result =  sum(students[i][1:4])
    print(f"Nom: {students[i][0]}, Note moyenne: {result/3}")


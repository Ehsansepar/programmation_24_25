# 5) Réalise un programme qui permet de supprimer les espaces dans une phrase (! 2 variables)
# Ex: il fait froid
# ilfaitfroid
# utilise un accumulateur dans lequel tu places uniquement les lettres.
# Ou utilise replace.

phrase = str(input("Entrez une phrase : "))

for i in  phrase:
    if i == " " :
        phrase = phrase.replace(" ", "")
print(phrase)
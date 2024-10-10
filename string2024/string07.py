# 7) Soit une variable m qui contient "la t§l§vision est cass§e, il faut la r§parer". Etablir un
# programme qui passe en revue cette chaîne et qui en construit une autre m2 où les § sont remplacés
# par é. (2 versions avec ou sans replace() )
#
m = input("Entrez une phrase : ")
m2 = m.replace("§", "é")

print(m2)
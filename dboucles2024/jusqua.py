import random

compteur  = 0

while True : 
    nombre = random.randint(1, 100)
    compteur  += 1
    print(f"nombre de Tire  : {compteur} :=>  {nombre}")

    if nombre == 75 : 
        break
print(f"Nombre de tirages nécessaires pour obtenir 75: {compteur}")
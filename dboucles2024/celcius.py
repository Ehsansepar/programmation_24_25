# Ecrivez un programme qui permet de transformer une température en degrés celcius en degrés
# farenheit. Tf = (Tc * 9/5 ) + 32 
# (celcius.py) (1, 2, 3, 4)
# Ex.
# Introduisez la temperature (celcius) 37
# La temperature en farenheit est de 98.6

Tc = float(input("Introduisez la temperature (celcius) : "))
Tf = (Tc * 9/5 ) + 32

print(f"La temperature en farenheit est de {Tf}")  
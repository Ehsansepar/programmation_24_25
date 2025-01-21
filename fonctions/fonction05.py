def nomMois(n) : 
    mois = [
        "Janvier", 
        "Février",
        "Mars",
        "Avril",
        "Mai",
        "Juin",
        "Juillet",
        "Août",
        "Septembre",
        "Octobre",
        "Novembre",
        "Décembre"
]
    if 1 <= n <= 12 : 
        return mois[(n-1)]
    else : 
        return None

print(nomMois(4))
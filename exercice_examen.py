# ===============================================
# EXERCICES TYPES POUR EXAMEN PYTHON
# ===============================================

print("=" * 50)
print("EXERCICES PYTHON - PRÉPARATION EXAMEN")
print("=" * 50)

#! ==============================================================================================
# EXERCICE 1: GESTION DE NOTES D'ÉTUDIANTS
# ===============================================

print("\n--- EXERCICE 1: GESTION DE NOTES ---")

# Base de données des notes
notes_etudiants = {
    "Alice": [15, 18, 12, 16],
    "Bob": [11, 13, 10, 14],
    "Charlie": [19, 16, 20, 18],
    "Diana": [8, 12, 9, 11]
}

def calculer_moyenne(nom):
    """Calcule la moyenne d'un étudiant"""
    if nom in notes_etudiants:
        notes = notes_etudiants[nom]
        return sum(notes) / len(notes)
    return None

def meilleur_etudiant():
    """Trouve l'étudiant avec la meilleure moyenne"""
    meilleur = ""
    meilleure_moyenne = 0
    
    for nom in notes_etudiants:
        moyenne = calculer_moyenne(nom)
        if moyenne and moyenne > meilleure_moyenne:
            meilleure_moyenne = moyenne
            meilleur = nom
    
    return meilleur, meilleure_moyenne

def etudiants_au_dessus_moyenne():
    """Trouve les étudiants au-dessus de la moyenne générale"""
    # Calculer moyenne générale
    toutes_notes = []
    for notes in notes_etudiants.values():
        toutes_notes.extend(notes)
    moyenne_generale = sum(toutes_notes) / len(toutes_notes)
      # Trouver étudiants au-dessus
    etudiants_reussis = []
    for nom in notes_etudiants:
        moyenne = calculer_moyenne(nom)
        if moyenne and moyenne > moyenne_generale:
            etudiants_reussis.append(nom)
    
    return etudiants_reussis, moyenne_generale

# Tests
print("Moyennes des étudiants:")
for nom in notes_etudiants:
    print(f"{nom}: {calculer_moyenne(nom):.2f}")

meilleur, moyenne = meilleur_etudiant()
print(f"\nMeilleur étudiant: {meilleur} avec {moyenne:.2f}")

reussis, moy_gen = etudiants_au_dessus_moyenne()
print(f"Moyenne générale: {moy_gen:.2f}")
print(f"Étudiants au-dessus: {reussis}")

#! =============================================================================================================================================
# EXERCICE 2: INVENTAIRE MAGASIN
# ===============================================

print("\n" + "=" * 50)
print("--- EXERCICE 2: INVENTAIRE MAGASIN ---")

# Base de données produits
inventaire = {
    "pommes": {"prix": 2.5, "stock": 50},
    "bananes": {"prix": 1.8, "stock": 30},
    "oranges": {"prix": 3.0, "stock": 25},
    "poires": {"prix": 2.8, "stock": 15}
}

def afficher_inventaire():
    """Affiche tout l'inventaire"""
    print("\nINVENTAIRE ACTUEL:")
    print("-" * 30)
    for produit, info in inventaire.items():
        print(f"{produit.capitalize()}: {info['prix']}€ - Stock: {info['stock']}")

def valeur_totale_stock():
    """Calcule la valeur totale du stock"""
    total = 0
    for produit, info in inventaire.items():
        total += info['prix'] * info['stock']
    return total

def produits_en_rupture():
    """Trouve les produits avec stock < 20"""
    rupture = []
    for produit, info in inventaire.items():
        if info['stock'] < 20:
            rupture.append(produit)
    return rupture

def acheter_produit(produit, quantite):
    """Simule l'achat d'un produit"""
    if produit in inventaire:
        if inventaire[produit]['stock'] >= quantite:
            inventaire[produit]['stock'] -= quantite
            prix_total = inventaire[produit]['prix'] * quantite
            return f"Achat réussi! Total: {prix_total:.2f}€"
        else:
            return f"Stock insuffisant! Disponible: {inventaire[produit]['stock']}"
    else:
        return "Produit non trouvé!"

# Tests
afficher_inventaire()
print(f"\nValeur totale du stock: {valeur_totale_stock():.2f}€")
print(f"Produits en rupture (< 20): {produits_en_rupture()}")

print("\nSimulation d'achats:")
print(acheter_produit("pommes", 10))
print(acheter_produit("poires", 20))  # Pas assez de stock
afficher_inventaire()

#! ============================================================================================================================================================================================
# EXERCICE 3: JEU DEVINE LE NOMBRE
# ===============================================

print("\n" + "=" * 50)
print("--- EXERCICE 3: JEU DEVINE LE NOMBRE ---")

import random

def jeu_devine_nombre():
    """Jeu où l'ordinateur devine votre nombre"""
    print("\nPensez à un nombre entre 1 et 100!")
    print("Répondez par 'plus', 'moins' ou 'gagne'")
    
    min_val = 1
    max_val = 100
    tentatives = 0
    
    while True:
        tentatives += 1
        guess = (min_val + max_val) // 2
        
        print(f"\nTentative {tentatives}: Est-ce {guess}?")
        reponse = input("Votre réponse (plus/moins/gagne): ").lower()
        
        if reponse == "gagne":
            print(f"Gagné en {tentatives} tentatives!")
            break
        elif reponse == "plus":
            min_val = guess + 1
        elif reponse == "moins":
            max_val = guess - 1
        else:
            print("Réponse invalide! Utilisez: plus, moins, ou gagne")
        
        if min_val > max_val:
            print("Erreur: vos réponses sont contradictoires!")
            break

# Décommentez pour jouer:
# jeu_devine_nombre()

#! =============================================================================================================================================
# EXERCICE 4: ANALYSE DE TEXTE
# ===============================================

print("\n" + "=" * 50)
print("--- EXERCICE 4: ANALYSE DE TEXTE ---")

def analyser_texte(texte):
    """Analyse complète d'un texte"""
    # Nettoyer le texte
    texte = texte.lower()
    mots = texte.split()
    
    # Statistiques de base
    nb_caracteres = len(texte)
    nb_mots = len(mots)
    nb_phrases = texte.count('.') + texte.count('!') + texte.count('?')
    
    # Compter les mots
    compteur_mots = {}
    for mot in mots:
        # Enlever la ponctuation
        mot_propre = mot.strip('.,!?;:')
        if mot_propre:
            compteur_mots[mot_propre] = compteur_mots.get(mot_propre, 0) + 1    # Mot le plus fréquent
    if compteur_mots:
        mot_frequent = max(compteur_mots.keys(), key=lambda x: compteur_mots[x])
    else:
        mot_frequent = ""
      return {
        'caracteres': nb_caracteres,
        'mots': nb_mots,
        'phrases': nb_phrases,
        'mot_frequent': (mot_frequent, compteur_mots.get(mot_frequent, 0) if mot_frequent else 0),
        'compteur': compteur_mots
    }

# Test
texte_exemple = """
Python est un langage de programmation. 
Python est facile à apprendre et Python est puissant.
Beaucoup de développeurs aiment Python!
"""

resultats = analyser_texte(texte_exemple)
print("ANALYSE DU TEXTE:")
print(f"Caractères: {resultats['caracteres']}")
print(f"Mots: {resultats['mots']}")
print(f"Phrases: {resultats['phrases']}")
print(f"Mot le plus fréquent: {resultats['mot_frequent'][0]} ({resultats['mot_frequent'][1]} fois)")

#! ============================================================================================================================================================================================
# EXERCICE 5: CARNET D'ADRESSES
#! ===============================================

print("\n" + "=" * 50)
print("--- EXERCICE 5: CARNET D'ADRESSES ---")

carnet = {
    "Alice": {"telephone": "0123456789", "email": "alice@email.com", "ville": "Paris"},
    "Bob": {"telephone": "0987654321", "email": "bob@email.com", "ville": "Lyon"},
    "Charlie": {"telephone": "0555666777", "email": "charlie@email.com", "ville": "Paris"}
}

def ajouter_contact(nom, telephone, email, ville):
    """Ajoute un nouveau contact"""
    carnet[nom] = {
        "telephone": telephone,
        "email": email,
        "ville": ville
    }
    return f"Contact {nom} ajouté!"

def chercher_contact(nom):
    """Cherche un contact par nom"""
    if nom in carnet:
        return carnet[nom]
    return "Contact non trouvé"

def contacts_par_ville(ville):
    """Trouve tous les contacts d'une ville"""
    contacts = []
    for nom, info in carnet.items():
        if info['ville'].lower() == ville.lower():
            contacts.append(nom)
    return contacts

def afficher_carnet():
    """Affiche tout le carnet"""
    print("\nCARNET D'ADRESSES:")
    print("-" * 40)
    for nom, info in carnet.items():
        print(f"{nom}: {info['telephone']} | {info['email']} | {info['ville']}")

# Tests
afficher_carnet()
print(f"\nContacts à Paris: {contacts_par_ville('Paris')}")
print(ajouter_contact("Diana", "0111222333", "diana@email.com", "Marseille"))
print(f"Info Alice: {chercher_contact('Alice')}")

# !=============================================================================================================================================
# EXERCICE 6: CALCULATRICE AVANCÉE
# ===============================================

print("\n" + "=" * 50)
print("--- EXERCICE 6: CALCULATRICE ---")

def calculatrice(operation, a, b):
    """Calculatrice avec gestion d'erreurs"""
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            if b == 0:
                return "Erreur: Division par zéro!"
            return a / b
        elif operation == "**":
            return a ** b
        else:
            return "Opération non supportée"
    except Exception as e:
        return f"Erreur: {e}"

def calculer_liste_operations(operations):
    """Calcule une liste d'opérations"""
    resultats = []
    for op, a, b in operations:
        resultat = calculatrice(op, a, b)
        resultats.append(f"{a} {op} {b} = {resultat}")
    return resultats

# Tests
operations_test = [
    ("+", 10, 5),
    ("-", 10, 3),
    ("*", 7, 6),
    ("/", 15, 3),
    ("/", 10, 0),  # Test division par zéro
    ("**", 2, 8)
]

print("RÉSULTATS DES CALCULS:")
for resultat in calculer_liste_operations(operations_test):
    print(resultat)

print("\n" + "=" * 50)
print("FIN DES EXERCICES - BONNE CHANCE POUR L'EXAMEN!")
print("=" * 50)

# dictionnaire : représente les réponse d une personn e
# fontionj poser des questions et mémoriser les r eponses dans le dictionnaire
# fontion corriger (attribuer des points sur bases des reponses)


# key = pseudo
# reponses = {pseudo : "charles",
#           questionnaire : {Q1 : 1,
#                            Q2 : 2,
#                            Q3 : 3,
#                            Q4 : 4,
#                            Q5 : 5},
#           resultat : 23
#           }
#
#
#
#

def poser_questions(pseudo):
    """Placeholder for asking questions."""
    print(f"Questions posées à {pseudo}.")
    reponses = {}
    questions = [
        "Quelle est la capitale de la France ?",
        "Combien de jours y a-t-il dans une semaine ?",
        "Quelle couleur obtient-on en mélangeant le bleu et le jaune ?",
        "Quel est le plus grand océan du monde ?",
        "Combien font 2 + 2 ?"
    ]
    for i, q_text in enumerate(questions):
        reponse = input(f"Question {i+1}: {q_text} ")
        reponses[f"Q{i+1}"] = reponse
    return reponses
    return {} # Example: return a dictionary of answers

def calculer_correction(pseudo, reponses):
    """Calcule le score en comparant directement les réponses."""
    print(f"Correction pour {pseudo}.")
    score = 0
    reponses_correctes = {
        "Q1": "Paris",
        "Q2": "7",
        "Q3": "Vert",
        "Q4": "Pacifique",
        "Q5": "4"
    }

    for cle_question, reponse_utilisateur in reponses.items():
        if cle_question in reponses_correctes and reponse_utilisateur == reponses_correctes[cle_question]:
            score += 1
    
    print(f"Le score de {pseudo} est de {score}/{len(reponses_correctes)}")
    return score

def afficher_resultat(pseudo, resultat):
    """Placeholder for displaying results."""
    print(f"Résultat pour {pseudo}: {resultat}")
    # Implement result display logic here

continuer = True
pseudo_utilisateur = ""
reponses_utilisateur = {}
resultat_utilisateur = 0

while continuer:
    print("-" * 50)
    print("1. Répondre aux questions")
    print("2. Calculer le résultat")
    print("3. Afficher le résultat")
    print("4. Quitter")
    print("-" * 50)

    try:
        choix = int(input("Choisissez une option : "))

        if choix == 1:
            pseudo_utilisateur = input("Entrez votre pseudo : ")
            reponses_utilisateur = poser_questions(pseudo_utilisateur)
        elif choix == 2:
            if not pseudo_utilisateur:
                print("Veuillez d'abord répondre aux questions (option 1).")
            else:
                resultat_utilisateur = calculer_correction(pseudo_utilisateur, reponses_utilisateur)
                print("Résultat calculé.")
        elif choix == 3:
            if not pseudo_utilisateur:
                print("Veuillez d'abord répondre aux questions (option 1) et calculer le résultat (option 2).")
            else:
                afficher_resultat(pseudo_utilisateur, resultat_utilisateur)
        elif choix == 4:
            print("Au revoir !")
            continuer = False
        else:
            print("Option invalide. Veuillez choisir un nombre entre 1 et 4.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")


    # pseudo = input("Entrez votre pseudo : ")
    # repnses = poserQuestions(pseudo)
    # resultat = correction(pseudo)
    # continuer = False


    
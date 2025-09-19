print("saisir un nombre entre 1 et 12 :")
nombre = int(input())
def mois_lettre(n):
    mois = {
        1: "Janvier",
        2: "Février",
        3: "Mars",
        4: "Avril",
        5: "Mai",
        6: "Juin",
        7: "Juillet",
        8: "Août",
        9: "Septembre",
        10: "Octobre",
        11: "Novembre",
        12: "Décembre"
    }
    
    if n in mois:
        print(f"Le mois correspondant au nombre {n} est {mois[n]}.")
    else:
        print("Nombre invalide, veuillez saisir un nombre entre 1 et 12.")
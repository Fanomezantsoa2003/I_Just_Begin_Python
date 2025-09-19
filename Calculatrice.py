def calculer_expression(probleme):
    part = probleme.split()
    if len(part) < 3:  # Vérifier qu'il y a au moins une opération complète
        return "Expression invalide"
    
    # Commencer avec le premier nombre
    resultat = int(part[0])
    
    # Parcourir les opérateurs et nombres suivants
    i = 1
    while i < len(part):
        if part[i] in ["+", "-", "*", "/"]:
            operateur = part[i]
            
            # Vérifier qu'il y a un nombre après l'opérateur
            if i + 1 >= len(part):
                return "Expression invalide: opérateur sans nombre"
                
            try:
                nombre = int(part[i + 1])
            except ValueError:
                return "Expression invalide: ce n'est pas un nombre"
            
            # Effectuer l'opération
            if operateur == "+":
                resultat += nombre
            elif operateur == "-":
                resultat -= nombre
            elif operateur == "*":
                resultat *= nombre
            elif operateur == "/":
                if nombre == 0:
                    return "Erreur: Division par zéro"
                resultat /= nombre
            
            i += 2  # Passer à l'opérateur suivant
        else:
            return f"Opérateur non reconnu: {part[i]}"
    
    return resultat

def formater_probleme(probleme):
    formated = ''
    i = 0
    while i < len(probleme):
        formated += probleme[i]
        if probleme[i] != ' ':
            # Si le caractère suivant existe et n'est pas >
            if i + 1 < len(probleme) and probleme[i + 1]:
                formated += ' '
        i += 1
    return formated

# Programme principal
probleme = input("Entrer le problème: ")
probleme_formated = formater_probleme(probleme)
resultat = calculer_expression(probleme_formated)
print(f"Résultat: {resultat}")

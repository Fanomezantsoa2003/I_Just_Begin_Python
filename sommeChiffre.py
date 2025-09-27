print("Entrer un nombre :")
nombre = input()  # on garde la saisie comme chaîne

somme = 0
for chiffre in nombre:
    somme += int(chiffre)

print("La somme des chiffres est :", somme)

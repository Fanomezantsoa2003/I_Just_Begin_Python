print("Entrer un nombre :")
nombre = input()

somme = 0
for chiffre in nombre:
    somme += int(chiffre)

print("La somme des chiffres est :", somme)

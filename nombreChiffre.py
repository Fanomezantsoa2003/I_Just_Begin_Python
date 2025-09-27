print("entrer un nombre :")
nombre = int(input())

nombre = []

#compter les chiffres
for i in str(nombre):
    nombre.append(i)
print("le nombre de chiffre est de :", len(nombre))
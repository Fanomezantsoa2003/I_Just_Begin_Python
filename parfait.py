print("entrer un nombre :")
nombre = int(input())
sommeDiviseur = 0

for i in range(nombre):
    if i == 0:
        continue
    if nombre % i == 0:
        sommeDiviseur += i
        if sommeDiviseur == nombre:
            print("le nombre est parfait")
        else:
            print("le nombre n'est pas parfait")
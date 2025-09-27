print("entrer un nombre :")
nombre = int(input())

fact = 1

for i in range(nombre + 1):
    if i == 0 or i == 1:
        continue
    fact = fact * i
    
print("la factorielle de", nombre, "est", fact)
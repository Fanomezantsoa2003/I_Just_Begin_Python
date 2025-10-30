li = input("Entrer les éléments séparés par une espace").split()
li = [int(i) for i in li]

print("List:", li)

total = 0
for i in li:
    total += i

print("Somme:", total)

print("Entrer un nombre :")
nombre = int(input())

for i in range(1, nombre):
    j = i
    while j <= i:
        if i % 2 == 0:
            break
        else:
            print(i)
        j += 1

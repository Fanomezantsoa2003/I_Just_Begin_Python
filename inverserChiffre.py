print("entrer un nombre :")
nombre = int(input())

chiffres = []

# for i in str(nombre):
#     chiffres.append(i)
# chiffres.reverse()
# print("le nombre inversé est :", ''.join(chiffres))

for i in str(nombre):
    chiffres.append(i)
print(chiffres[-1::-1])

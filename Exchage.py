print("entrer le premier nombre (A): ")
A = int(input())
print("entrer le deuxieme nombre (B): ")
B = int(input())

def echanger(a, b):
    print("avant l'echange : " "A = ", a , "B = ", b)
    a, b = b, a
    print("apres l'echange : " "A = ", b , "B = ", a)
    return a, b

A, B = echanger(A, B)
print("A = ", A)
print("B = ", B)


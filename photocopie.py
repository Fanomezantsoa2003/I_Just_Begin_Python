print("entrer le nombre de photocopie :")
n = int(input())

if n <= 10:
    prix = n * 0.25
elif n <= 20 and n > 10:
    prix = n * 0.20
elif n > 20:
    prix = n * 0.10
    
print(f"le prix total est de : {prix} DH")
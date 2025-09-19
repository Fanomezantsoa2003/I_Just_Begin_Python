print("saisir nombre :")
nombre = int(input())
def pair_impair(n):
    if n % 2 == 0:
        print(f"{n} est pair")
    else:
        print(f"{n} est impair")
        
pair_impair(nombre)
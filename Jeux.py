import random
import tkinter as tk

nbr_aleatoire = random.randint(1, 100)

def rejouer():
    global nbr_aleatoire
    nbr_aleatoire = random.randint(1, 10)
    input.delete(0, tk.END)  # Effacer l'input
    bouton.config(state=tk.NORMAL)  # Réactiver le bouton
def bouton_click():
    # Récupérer le texte de l'input
    texte_input = input.get()
    # Convertir en entier
    nombre = int(texte_input)
    
    # Vérifier si le nombre est correct
    if nombre == nbr_aleatoire:
        print("Bravo, vous avez trouvé le nombre !")
        bouton.config(state=tk.DISABLED)  # Désactiver le bouton
    elif nombre > nbr_aleatoire:
        print("Le nombre est plus petit.")
    else: 
        print("Le nombre est plus grand.")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeux de hazard")
fenetre.geometry("300x200")

# Création input
input = tk.Entry(fenetre, width=20)
input.pack(pady=10)
# Création du bouton
bouton = tk.Button(fenetre, text="OK", command=bouton_click)
bouton.pack(pady=10)
retry = tk.Button(fenetre, text="Rejouer", command=rejouer)
retry.pack(pady=10)
fenetre.mainloop()

class Livre:
    def __init__(self ,titre , auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre}-{self.auteur}"


class Pile:
    def __init__(self):
        self.livres = []
    

    # fonction d'ajout des livre
    def push(self, livre):
        self.livres.append(livre)
        print(f"Vous avez ajouté {livre} à la pile.")

    # fonction pour retirerun livre
    def pop(self):
        if not self.is_empty():
            livre_retire = self.livres.pop()
            print(f"Vous avez retiré {livre_retire} de la pile.")
            return livre_retire
        else:
            print("La pile est vide.")
            return None
    

    # fontion pour voir le livre qui est en haut de la pile 
    def is_empty(self):
        return len(self.livres) == 0
    

    # fonction pour verifier si la pile est vide
    def peek(self):
        if not self.is_empty():
            return self.livres[-1]
        else:
            print("La pile est vide.")
            return None



def main():
    pile = Pile()

    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Ajouter un livre (push)")
        print("2. Retirer un livre (pop)")
        print("3. Vérifier si la pile est vide (is_empty)")
        print("4. Voir le livre en haut de la pile (peek)")
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5) : ")


        if choix == "1":
            titre = input("entrerle titre du livre:")
            auteur = input("entrer le nom de l'auteur:")
            livre = Livre(titre, auteur)
            pile.push(livre)
        elif choix == "2":
            pile.pop()
        elif choix == "3":
            if pile.is_empty():
                print("la pile est vide merci!!!")
            else:
                ("la pile n'est pas vide merci!!!")
        elif choix == "4":
            livre_haud = pile.peek()
            if livre_haud:
                print(f"le livre en haut de la pile est {livre_haud}")
        elif choix == "5":
            print("au revoir!!!")
            break
        else:
            print("choix invalide viellez reesayer merci!!!")
    
if __name__ == "__main__":
    main()


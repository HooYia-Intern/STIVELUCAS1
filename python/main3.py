class Client:
    def __init__(self, nom, panier):
        self.nom = nom
        self.panier = panier

    def __str__(self):
        return f"{self.nom} avec {self.panier} articles"

class File:
    def __init__(self):
        self.clients = []

    def enqueue(self, client):
        self.clients.append(client)
        print(f"Vous avez ajouté {client} à la file d'attente.")

    def dequeue(self):
        if not self.is_empty():
            client_retire = self.clients.pop(0)
            print(f"Vous avez retiré {client_retire} de la file d'attente.")
            return client_retire
        else:
            print("La file d'attente est vide.")
            return None

    def is_empty(self):
        return len(self.clients) == 0

    def peek(self):
        if not self.is_empty():
            return self.clients[0]
        else:
            print("La file d'attente est vide.")
            return None

    def afficher_file(self):
        if not self.is_empty():
            print("Clients dans la file d'attente :")
            for client in self.clients:
                print(client)
        else:
            print("La file d'attente est vide.")

def main():
    file_attente = File()

    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Ajouter un client (enqueue)")
        print("2. Retirer un client (dequeue)")
        print("3. Vérifier si la file est vide (is_empty)")
        print("4. Voir le client en tête de file (peek)")
        print("5. Afficher la file d'attente")
        print("6. Quitter")

        choix = input("Entrez votre choix (1-6) : ")

        if choix == "1":
            nom = input("Entrez le nom du client : ")
            panier = int(input("Entrez le nombre d'articles dans le panier : "))
            client = Client(nom, panier)
            file_attente.enqueue(client)

        elif choix == "2":
            file_attente.dequeue()

        elif choix == "3":
            if file_attente.is_empty():
                print("La file d'attente est vide.")
            else:
                print("La file d'attente n'est pas vide.")

        elif choix == "4":
            client_tete = file_attente.peek()
            if client_tete:
                print(f"Le client en tête de file est : {client_tete}")

        elif choix == "5":
            file_attente.afficher_file()

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
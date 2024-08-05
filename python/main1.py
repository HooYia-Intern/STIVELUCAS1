import os
from datetime import datetime

def main():
    while True:
        print('welcome to the dictionary file!!!')
        print("que voulez vus faire aujoudhui???")
        print("1.creer un fichier")
        print("2.modifier un fichier")
        print("3.supprimer  un fichier")
        print("4.acceder a un fichier")
        print("5.renommer un fichier")
        print("6.deplacer un fichier un fichier")
        print("7. Rechercher et remplacer dans un fichier")
        print("8. Ouvrir et fermer un fichier")
        print("9.lister l'ensemble avec leur informations de vos fichiers")
        print("10. quitter")

        choice = input("svp viellez entrer l'une des options entre (1-10): ")

        if choice == "1":
            create_file()
        elif choice == "2":
            modify_file()
        elif choice == "3":
            delete_file()
        elif choice == "4":
            access_file()
        elif choice == "5":
            rename_file()
        elif choice == "6":
            move_file()
        elif choice == "7":
           search_file()
        elif choice == "8":
            open_and_close_file()
        elif choice == "9":
            list_files()
        elif choice == "10":
            print("au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")




# declaration de la fonction qui doit permettre la creation de 'un fichier
def create_file():
    filename = input("Entrez le nom du fichier à créer :\n ")
    try:
        with open(filename, "w") as file:
            print(f"Le fichier {filename} a été créé.")
    except IOError:
        print(f"Impossible de créer le fichier {filename}.")

# fonction pour la modification du fchier a la l'attribut write
def modify_file():
    filename = input("entrer le nom du fichier a modifier\n")
    try:
        with open(filename, "a") as file:
            new_content = input("entrer le nouveau contenue a modifier")
            file.write(new_content)
            print(f"le fichier {filename} a ete modifier")
    except IOError:
        print(f"impossible de modifier le fichier {filename}")



# declaration de la fonction delete a l'aide de l'attribut remove
def delete_file():
    filename = input("entrer le nom du fichier a supprimer\n")
    try:
        os.remove(filename)
        print(f"le fichier {filename} a ete supprimer avec succes")
    except IOError:
        print(f"le fichier {filename} ne peut etre supprimer merci!!")



# fonction d'acces au fichier
def  access_file():
    filename= input("entrer le nom du fichier que vous voulez acceder\n")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"le contenu du fichier {filename}est\n : {content}")
    except IOError:
        print(f"impossible d'acceder au fichier {filename}")


# fonction pour renommer un fichier a l'aide de l'attribut rename
def rename_file():
    old_file = input("entrer le nom de l'ancien fichier a modifier\n")
    new_file = input("entrer le nom du nouveau fichier\n")
    try:
        os.rename( old_file,  new_file )
        print(f"le fichier {old_file} a ete renomme en fichier {new_file} avec succes merci!!!")
    except IOError:
        print(f"impossible d renomme le fichier {old_file}")



# fonction pour deplacer un fichier 
def  move_file():
    filename = input("entrer le nom du fichier a deplacer :")
    new_location = input("entrer le nouveau chemin du depot du fichier")
    try:
        os.rename( filename , os.path.join(filename, *new_location))
        print(f"le fichier {filename} a ete deplacer vers {new_location}")
    except IOError:
        print(f"impossible de deplacer le fichier {filename}")

# fonction pour chercher un fichier dans le repertoire
def search_file(filename):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == filename:
                file_path = os.path.join(root, file)
                print(f"Fichier trouvé : {file_path}")
                return file_path
    print(f"Fichier '{filename}' non trouvé.")
    return None


# fonction pour ouvrir et fermer un fichier
def open_and_close_file():
    filename = input("entrer le nom di fichier aouvrir:")

    try:
        file = open(filename, "r")
        print(f"le fichier {filename} a ete ouvert merci")
        content = file.read
        print(f"le contenue du fichier {filename} est \n:{content}")

        file.close()
        print(f"le fichier {filename} a ete ferme avec succes merci")
    except IOError:
        print(f"impossible d'ouvrir le fichier {filename} reessaye a nouveau merci!!")

# fonction pour lister l'ensemble des fichier creer
def list_files():
    print("voici la liste des fichiers cree :")
    for filename in os.listdir():
        file_path = os.path.join(os.getcwd(), filename)
        file_stats = os.stat(file_path)
        create_file = datetime.fromtimestamp(file_stats.st_ctime)
        print(f"nom : {filename}")
        print(f"chemin d'acces : {file_path}")
        print(f"date de creation du fichier : {create_file.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Taille : {file_stats.st_size} octets")
        print("-----------!!!!")



if __name__ == "__main__":
    main()
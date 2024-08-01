import sqlite3
import random
import string

class Student:
    def __init__(self, firstname, lastname, Email, phoneNumber, school, matricule=None):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__Email = Email
        self.__phoneNumber = phoneNumber
        self.__school = school
        self.__matricule = matricule if matricule else self.__generer_matricule()
        self.__conn = sqlite3.connect('database.db')
        self.__cursor = self.__conn.cursor()
        self.__create_table()

    def __generer_matricule(self):
        caracteres = string.ascii_uppercase + string.digits
        return ''.join(random.choice(caracteres) for _ in range(8))

    def __create_table(self):
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS comptes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT,
                lastname TEXT,
                Email TEXT,
                phoneNumber INTEGER,
                school TEXT,
                matricule TEXT
            )
        """)
        self.__conn.commit()

    def insert_student(self):
        self.__cursor.execute("INSERT INTO comptes (firstname, lastname, Email, phoneNumber, school, matricule) VALUES (?, ?, ?, ?, ?, ?)",
                             (self.__firstname, self.__lastname, self.__Email, self.__phoneNumber, self.__school, self.__matricule))
        self.__conn.commit()
        print(f"Student {self.__matricule} has been added.")

    def update_student(self, matricule):
        self.__cursor.execute("UPDATE comptes SET matricule = ? WHERE matricule = ?", (matricule, self.__matricule))
        self.__conn.commit()
        print(f"Student {matricule} was last updated.")

    def delete(self, matricule):
        self.__cursor.execute("DELETE FROM comptes WHERE matricule = ?", (matricule,))
        self.__conn.commit()
        print(f"Student {matricule} has been deleted.")

    def retrieve(self, matricule):
        self.__cursor.execute("SELECT * FROM comptes WHERE matricule = ?", (matricule,))
        result = self.__cursor.fetchone()
        if result:
            print(f"Firstname: {result[1]}, Lastname: {result[2]}, Email: {result[3]}, Phone Number: {result[4]}, School: {result[5]}, Matricule: {result[6]}")
        else:
            print(f"No student found for matricule {matricule}.")

    def list_all(self,):
        self.__cursor.execute("SELECT * FROM comptes")
        comptes = self.__cursor.fetchall()
        for compte in comptes:
            print(f"Firstname: {compte[1]}, Lastname: {compte[2]}, Email: {compte[3]}, Phone Number: {compte[4]}, School: {compte[5]}, Matricule: {compte[6]}")

    def __del__(self):
        self.__conn.close()


        
# Créer 3 objets Student avec les informations fournies
student1 = Student(firstname="Jean", lastname="Dupont", Email="jean.dupont@example.com", phoneNumber=625252525, school="Jeantapi")
student2 = Student(firstname="Marie", lastname="Leroy", Email="marie.leroy@example.com", phoneNumber=None, school=None)
student3 = Student(firstname="Pierre", lastname="Mercier", Email="pierre.mercier@example.com", phoneNumber=None, school=None)
student4 = Student(firstname="CEDRIC", lastname="elene", Email="jean.elene@example.com", phoneNumber=652595234, school="BIAST")
# Insérer les 3 étudiants dans la base de données
student1.insert_student()
student2.insert_student()
student3.insert_student()
student4.insert_student()

# Afficher les informations des 3 étudiants
student1.retrieve(student1._Student__matricule)
student2.retrieve(student2._Student__matricule)
student3.retrieve(student3._Student__matricule)
student4.retrieve(student4._Student__matricule)

#afficher la liste des etudiants
Student.list_all()

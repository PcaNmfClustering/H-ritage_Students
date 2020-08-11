#coding: uft-8
class Adulte(Personne):
    def __init__(self, nom,age,taille):
        self.nom = nom 
        self.age = age
        self.taille = taille
    def afficher(self):
        print("Le nom de la personne est : ", self.nom)
        print("L'age de la personne est : ",self.age)
        print("La taille de la personne est : ",self.taille)

class Etudiant(Personne):
    def __init__(self, nom, age, taille, filliere):
        Personne.__init__(self,nom,age,taille)
        self.filiere = filiere 
etudiant1 = Student("Joris", 14, "1m64" "Mathématiques")
etudiant1.afficher()
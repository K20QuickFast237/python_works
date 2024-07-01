from typing import List
from Ecole import *

class Personne:
    def __init__(self, nom):
        self.nom = nom.capitalize()
    
    def __str__(self):
        return f"Je suis {self.nom}"

    def __eq__(self, autre: 'Personne'):
        return self.nom == autre.nom


class Professeur(Personne):
    def __init__(self, nom, matiere):
        super().__init__(nom)
        self.matiere = matiere

    def __str__(self):
        return f"Je suis le prof {self.nom}, j'enseigne {self.matiere}."

    def isPrincipal(self, classe: Classe):
        if self == classe.principal:
            return True
        return False

    def affecter(self, classe: Classe):
        if self in classe.professeurs:
            return "Cet enseignant enseigne déjà dans la Classe."
        if not self.matiere.nom in classe.getMatieres():
            return "Cet Enseignat ne peut être ajouté,\nLa Classe ne dispense pas ça matière!"
        classe.professeurs.append(self)
        return True
            


class Eleve(Personne):
    def __init__(self, nom, classe: Classe, matieres: List[Matiere] = []):
        super().__init__(nom)
        self.classe   = classe
        self.matieres = matieres

    def __str__(self):
        return f"Je suis l'eleve {self.nom}"

    def suit(self, cours: 'Cours'):
        if not cours in self.cours:
            self.cours.append(cours)

    def inscrit(self, classe: 'Classe'):
        classe.eleves.append(self)

    def getMatieres(self):
        if not self.matieres == []:
            liste = []
            for matiere in self.matieres:
                liste.append(matiere.nom)
            return liste
        else:
            return self.classe.getMatieres()


class Administrateur(Personne):
    def __init__(self, nom="Admin"):
        super().__init__(nom)
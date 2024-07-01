from typing import List

class Matiere:
    def __init__(self, nom, coefficient=1):
        self.nom = nom.capitalize()
        self.coefficient = coefficient

    def __str__(self):
        # return f"{self.nom}: matière"
        return self.nom

    # def __eq__(self, autre: 'Matiere'):
    #     return self.nom == autre.nom



class Note:
    def __init__(self, valeur):
        self.valeur = valeur



class Session:
    def __init__(self, nom, eleves=[], matieres=[], notes=[]):
        self.nom      = nom.capitalize()
        self.eleves   = eleves
        self.matieres = matieres
        self.notes    = notes

    def __eq__(self, autre: 'Session'):
        return self.nom == autre.nom



class Cours:
    """"No more used"""
    def __init__(self, matiere, classe):
        self.matiere = matiere
        self.classe  = classe



class Classe:
    def __init__(self, nom, eleves=[], matieres=[], professeurs=[], sessions=[], **kwargs):
        self.nom         = nom.capitalize()
        self.eleves      = eleves
        self.matieres    = matieres
        self.professeurs = professeurs
        self.sessions    = sessions
        self.principal   = None
        for (key,val) in kwargs.items():
            setattr(self, key, val)
        
    def __str__(self):
        text = ""
        for (key,val) in self.__dict__.items():
            text += key+":"+str(val)+", "
        return text.strip(", ")

    def __eq__(self, autre: 'Classe'):
        return self.nom == autre.nom

    def getMatieres(self) -> List[str]:
        liste = []
        for elt in self.matieres:
            liste.append(elt.nom)
        return liste

    def ajouteMatiere(self, matiere: Matiere):
        self.matieres.append(matiere)

    def getProfesseurs(self) -> List[str]:
        liste = []
        for ens in self.professeurs:
            liste.append(ens.nom)
        return liste

    def getEleves(self) -> List[str]:
        liste = []
        for els in self.eleves:
            liste.append(els.nom)
        return liste

    def getSessions(self) -> List[str]:
        liste = []
        for elt in self.sessions:
            liste.append(elt.nom)
        return liste

    def ajouteSession(self, session: Session):
        self.sessions.append(session)


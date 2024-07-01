from Ecole import *
from Personnes import *
from tabulate import tabulate 

class User(Personne):
    def __init__(self, nom, profil):
        super().__init__(nom)
        self.profil = profil
    
    def __str__(self):
        return super().__str__()

class App:
    admin     = Administrateur()
    users     = [User(admin.nom, "Admin")]
    eleves    = {}
    profs     = {}
    classes   = {}
    matieres  = {}
    curr_user = None

# Menu 
    def display_admin_menu(self):
        print("""
        +-----------------------------------------------------------+
        |                   Menu D'administration                   |
        +-----------------------------------------------------------+
            1- Ajouter une Classe
            2- Ajouter un  Enseignant
            3- Ajouter une Matière
            4- Ajouter un  Élève
            5- Voir toutes les Classes
            6- Voir tous   les Enseignants
            7- Voir toutes les Matières
            8- Voir tous   les Élèves
            0- Sortir
        Faites votre choix: """, end="")
    def manage_admin_menu(self, choise: int):
        if choise == 1:
            self.addClasse()
        if choise == 2:
            self.addEnseignant()
        if choise == 3:
            self.addMatiere()
        if choise == 4:
            self.addEleve()
        if choise == 5:
            classes = []
            # print(self.classes)
            for classe in self.classes:
                # print(classe)
                # classes.append(self.classes[classe.nom.lower()].__dict__)
                # classes.append(classe.__dict__)
                classes.append(self.classes[classe.lower()].__dict__)
            if classes == []:
                print("Aucune Classe disponible pour le moment.")
            else:
                self.showInTable(classes)
        if choise == 6:
            profs = []
            for user in self.users:
                if user.profil == "Prof":
                    profs.append(self.profs[user.nom.lower()].__dict__)
            if profs == []:
                print("Aucun Enseignant disponible pour le moment.")
            else:
                self.showInTable(profs)
        if choise == 7:
            matieres = []
            for matiere in self.matieres:
                # matieres.append(self.matieres[matiere.nom].__dict__)
                matieres.append(self.matieres[matiere.lower()].__dict__)
            if matieres == []:
                print("Aucune Matière disponible pour le moment.")
            else:
                self.showInTable(matieres)
        if choise == 8:
            eleves = []
            for user in self.users:
                if user.profil == "Eleve":
                    eleves.append(self.eleves[user.nom].__dict__)
            if eleves == []:
                print("Aucun Eleve disponible pour le moment.")
            else:
                self.showInTable(eleves)
    
    def display_prof_menu(self):
        """Recupère la liste des classes du prof et affiche sous forme de mune"""
        menuProf = """"
        +-----------------------------------------------------------+
        |                     Espace Professeurs                    |
        +-----------------------------------------------------------+
        Vos classes :
            1- classe_name
            2- classe_name
            3- classe_name
        Faites votre choix: 
        """
        print("Menu des profs")
    def manage_prof_menu(self, choise: int):
        ...
    
    def display_eleve_menu(self):
        print("Menu des eleves")
    def manage_eleve_menu(self, choise: int):
        ...

    def display_classe_menu(self, classe: Classe):
        print(f"""
        +-----------------------------------------------------------+
        |        Gérer la classe {classe.nom}                       |
        +-----------------------------------------------------------+
            1- Ajouter une matiere  (Admins Only)
            2- Ajouter un  enseignant  (Admins Only)
            3- Ajouter un  eleve  (Admins Only)
            4- Ajouter une session  (Admins Only)
            5- Voir toutes les matieres
            6- Voir tous   les enseignants
            7- Voir tous   les eleves
            8- Voir toutes les sessions
            0- retour
        Faites votre choix: """, end="")
    def manage_classe_menu(self, classe: Classe, choise: int):
        if choise == 1:
            if not self.curr_user.profil == "Admin":
                self.show_access_denied()
                self.wait_before_continue()
                return
            matieres = list(self.matieres.keys())
            if not matieres == []:
                print("Matieres disponibles:")
                print(matieres)
            else:
                print("Aucune matière à ajouter pour le Moment...")
                self.wait_before_continue()
                return
            print("Matieres de la classe:")
            if mats:=classe.getMatieres():
                print(mats)
            else:
                print("Aucune matière dans la classe pour le moment...")
                # self.wait_before_continue()
            nom = self.get_string_input("Matière à ajouter: ", matieres)
            classe.ajouteMatiere(self.matieres[nom])
            print("Matière ajoutée à la Classe!")
            self.wait_before_continue()
        if choise == 2:
            # restrindre la fonctionalité uniquement aux administrateurs
            if not self.curr_user.profil == "Admin":
                self.show_access_denied()
                self.wait_before_continue()
                return
            # profs = list(self.profs.keys())
            profs = self.getAvailableProfsForClass(classe)
            if not profs == []:
                print("Enseignants disponibles:")
                print(profs)
            else:
                print("Aucun Enseignant à ajouter pour les matières de la classe...")
                self.wait_before_continue()
                return
            print("Enseignants de la classe:")
            if ens:=classe.getProfesseurs():
                print(ens)
            else:
                print("Aucun Enseignant dans la classe pour le moment.")
            nom = self.get_string_input("Enseignant à ajouter: ", profs)
            # msg = classe.ajouteProfesseur(self.profs[nom])
            msg = self.profs[nom.lower()].affecter(classe)
            if msg == True:
                print("Enseignant ajouté à la classe!")
            else:
                print(msg)
            self.wait_before_continue()
        if choise == 3:
            if not self.curr_user.profil == "Admin":
                self.show_access_denied()
                return
            eleves = list(self.eleves.keys())
            if not eleves == []:
                print("Eleves disponibles:")
                print(eleves)
            else:
                print("Aucun Eleve à ajouter pour le Moment...")
                self.wait_before_continue()
                return
            print("Eleves de la classe:")
            if els:=classe.getEleves():
                print(els)
            else:
                print("Aucun Eleve dans la classe pour le moment.")
            nom = self.get_string_input("Eleve à ajouter: ", eleves)
            # classe.ajouteEleve(self.eleves[nom])
            self.eleves[nom].inscrit(classe)
            print("Eleve ajouté à la Classe!")
            self.wait_before_continue()
        if choise == 4:
            if not self.curr_user.profil == "Admin":
                self.show_access_denied()
                self.wait_before_continue()
                return
            sess = list(self.sessions.keys())
            if not sess == []:
                print("Sessions disponibles:")
                print(sess)
            else:
                print("Aucune Session à ajouter pour le Moment...")
                self.wait_before_continue()
                return
            print("Sessions de la classe:")
            if ses:=classe.getSessions():
                print(ses)
            else:
                print("Aucune Session dans la classe pour le moment.")
            nom = self.get_string_input("Session à ajouter: ", sess)
            classe.ajouteSession(self.sessions[nom])
            print("Session ajoutée à la Classe!")
            self.wait_before_continue()
        if choise == 5:
            matieres = []
            for matiere in classe.matieres:
                matieres.append(matiere.__dict__)
            if matieres == []:
                print("Aucune Matière dans cette classe pour le moment.")
            else:
                self.showInTable(matieres)
            self.wait_before_continue()
        if choise == 6:
            profs = []
            for prof in classe.professeurs:
                profs.append(self.profs[prof.nom.lower()].__dict__)
            if profs == []:
                print("Aucun Enseignant dans cette classe pour le moment.")
            else:
                # print(profs)
                self.showInTable(profs)
            self.wait_before_continue()
        if choise == 7:
            eleves = []
            for eleve in classe.eleves:
                eleves.append(eleve.__dict__)
            if eleves == []:
                print("Aucun Eleve dans cette classe pour le moment.")
            else:
                self.showInTable(eleves)
            self.wait_before_continue()
        if choise == 8:
            sessions = []
            for session in classe.sessions:
                sessions.append(session.__dict__)
            if sessions == []:
                print("Aucuns Session dans cette classe pour le moment.")
            else:
                self.showInTable(sessions)
            self.wait_before_continue()

    def play(self, player: User):
        """Boucle de fonctionnement du l'app """
        self.curr_user = player
        while True:
            display = f"display_{player.profil.lower()}_menu"
            getattr(self, display)()
            choix  = self.get_integer_input()
            if choix == 0:
                break
            action = f"manage_{player.profil.lower()}_menu"
            getattr(self, action)(choix)
            self.wait_before_continue()


# Level 2
    """
        def showEleves(self, eleves):
            print(tabulate(eleves, headers="keys", tablefmt="pretty"))

        def showClasses(self, classes):
            print(tabulate(classes, headers="keys", tablefmt="pretty"))

        def showMatieres(self, matieres):
            print(tabulate(matieres, headers="keys", tablefmt="pretty"))

        def showProfs(self, profs):
            print(tabulate(profs, headers="keys", tablefmt="pretty"))

        def showSessions(self, sess):
            print(tabulate(sess, headers="keys", tablefmt="pretty"))
    """
    def showInTable(self, elments: List[object]):
        print(tabulate(elments, headers="keys", tablefmt="pretty"))
    
    def addMatiere(self):
        nom  = self.get_string_input("Quel est le nom de la matière: ").casefold()
        # coef = self.get_integer_input("Quel est son coefficient: ")
        for name in self.matieres.keys():
            if nom == name:
                print("Cette matiere existe déjà")
                break
        else:
            matiere = Matiere(nom)
            self.matieres[nom] = matiere
            print("La matiere a bien été ajoutée")
    def addClasse(self):
        nom = self.get_string_input("Quel est le nom de la classe: ").casefold()
        for name in self.classes.keys():
            if nom == name:
                print("Cette Classe existe déjà!")
                break
        else:
            classe = Classe(nom)
            self.classes[nom] = classe
            self.manageClasse(classe) 
    def getAvailableProfsForClass(self, classe: Classe):
        # retourner uniquement les profs pouvant enseigner les matières de la classe
        profs = self.profs.values()
        matieres = [matiere.nom.casefold() for matiere in classe.matieres]
        classProfs = []
        for prof in profs:
            if prof.matiere.nom.casefold() in matieres:
                classProfs.append(prof.nom)
        return classProfs
    def addEnseignant(self):
        nom = self.get_string_input("Quel est le nom de l'enseignant: ").casefold()
        matieres = list(self.matieres.keys())
        # On n'ajoute un enseignat que s'il y'a des matères disponibles à enseigner
        if not matieres == []:
            for name in self.profs.keys():
                if nom == name:
                    print("Cet Enseignant existe déjà!")
                    break
            else:
                print("Matières disponibles: ")
                matieres = list(self.matieres.keys())
                print(matieres)
                nom_matiere = self.get_string_input("Choisir sa matière dans la liste: ", matieres)
                prof = Professeur(nom, self.matieres[nom_matiere])
                user = User(nom, "Prof")
                self.profs[nom] = prof
                self.users.append(user)
                print("Enseignant Ajouté!")
        else:
            print("Aucune matière enregistrée dans le système, \nVous ne pouvez ajouter un enseignant.")
    def addEleve(self):
        nom = self.get_string_input("Quel est le nom de l'eleve: ").casefold()
        for name in self.eleves.keys():
            if nom == name:
                print("Cet Elève existe déjà!")
                break
        else:
            print("Classes disponibles: ")
            classes = list(self.classes.keys())
            print(classes)
            nom_classe = self.get_string_input("Choisir sa classe dans la liste: ", classes)
            eleve = Eleve(nom, self.classes[nom_classe])
            user = User(nom, "Eleve")
            self.eleves[nom] = eleve
            self.users.append(user)
            print("Eleve Ajouté!")

# Level 1
    def manageClasse(self, classe: Classe):
        while True:
            self.display_classe_menu(classe)
            choix  = self.get_integer_input()
            if choix == 0:
                return
            else:
                self.manage_classe_menu(classe, choix)
    def manageEnseignant(self, prof: Professeur):
        ...
    def manageEleve(self, eleve: Eleve):
        ...

# Utilities
    def get_string_input(self, prompt="", values=None):
        value = input(prompt).strip().casefold()
        while True:
            if values and (not value in values):
                print("Valeure incorrecte, Veuillez choisir une dans la liste.")
                value = input("Réesayez: ")
            else:
                return value
    def get_float_input(self, prompt="", values=None):
        while True:
            try:
                value = float(input(prompt).strip())
                if values and (not value in values):
                    print("Valeure incorrecte, Veuillez choisir une dans la liste.")
                else:
                    return value
            except:
                print("Valeure incorrecte.")
                if not prompt:
                    print("Réesayez: ", end="")
    def get_integer_input(self, prompt="", values=None): 
        while True:
            try:
                value = int(input(prompt).strip())
                if values and (not value in values):
                    print("Valeure incorrecte, Veuillez choisir une dans la liste.")
                else:
                    return value
            except:
                print("Valeure incorrecte.")
                if not prompt:
                    print("Réesayez: ", end="")

    def wait_before_continue(self):
        input("\nPressez Enter!")

    def show_access_denied(self):
        print("Désolé! Vous n'avez pas accès à cette zone.")


# Main
def main():
    app = App()
    nom = input("Entrez votre nom: ")
    user= None

    for user in App.users:
        if user.nom.casefold() == nom.casefold():
            user=user
            break
    if user:
        app.play(user)
    else:
        print("Identification incorrecte.", end="")
    
    exit("""
    +-----------------------------------------------------------+
    |                           Bye bye!                        |
    +-----------------------------------------------------------+""")


if __name__ == "__main__":
   main()
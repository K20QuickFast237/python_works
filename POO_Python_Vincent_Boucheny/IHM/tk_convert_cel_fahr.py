from tkinter import Frame, Label, Scale
from tkinter import LEFT, HORIZONTAL


class Mafenetre(Frame):
    # le paramètre correspond à l'élément le contenant
    def __init__(self, master = None):
        super(Mafenetre, self).__init__(master)
        self.master.title("Convertisseur C <==> F")
        # pack() permet de consolider la géométrie de la frame dans la fenêtre
        self.pack()

    def initWidgets(self):
        # Déclaration du label affichant le texte C
        self.Ctext = Label(self, text="C")
        # Déclaration d'un curseur qui affichera les degrés Celsius
        self.Ccurseur = Scale(self, from_=-100, to=100, orient=HORIZONTAL, command=self.convertirCEnF)
        # initialisation du curseur à 0
        self.Ccurseur.set(0)

        # Declaration du label affichant le texte F
        self.Ftext = Label(self, text="F")
        # Déclaration d'un curseur qui affichera les degrés Fahrenheit
        self.Fcurseur = Scale(self, from_=-148, to=212, orient=HORIZONTAL, command=self.convertirFEnC)
        # initialisation du curseur à 32
        self.Fcurseur.set(32)

        # Cree une liste de widgets sur laquelle on boucle
        for widget in [self.Ctext, self.Ccurseur, self.Ftext, self.Fcurseur]:
            # le widget courant est plaqué à gauche dans la fenêtre de l'app
            widget.pack(side=LEFT)


    def convertirCEnF(self, value):
        C = float(value)
        F = C * 9 / 5 + 32
        self.Fcurseur.set(F)

    def convertirFEnC(self, value):
        F = float(value)
        C = (F - 32) * 5 / 9
        self.Ccurseur.set(C)




...
if __name__ == "__main__":
    # Instanciation de la fenêtre
    ma_fenetre = Mafenetre()
    # Initialisation des widgets
    ma_fenetre.initWidgets()
    # Lancement de la boucle principale de l'IHM
    ma_fenetre.mainloop()

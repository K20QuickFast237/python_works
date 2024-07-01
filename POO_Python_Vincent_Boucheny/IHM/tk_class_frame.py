from tkinter import Frame

class Mafenetre(Frame):
    # le paramètre correspond à l'élément le contenant
    def __init__(self, master = None):
        super(Mafenetre, self).__init__(master, width = 320, height = 240)

        # la fenêtre contenant la frame est référencée par l'attribut master
        self.master.title("Mon application graphique")

        # pack() permet de consolider la géométrie de la frame dans la fenêtre
        self.pack()




...
if __name__ == "__main__":
    ma_fenetre = Mafenetre()
    ma_fenetre.mainloop()

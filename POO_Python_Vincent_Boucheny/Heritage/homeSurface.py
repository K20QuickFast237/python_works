# homeSurface.py

class Mur:
    def __init__(self, orientation):
        self.orientation = orientation
        # un mur n'a aucune fenêtre pqr dùefaut
        self.fenetres = []

class Fenetre:
    def __init__(self, mur, surface, protection):
        self.mur     = mur
        self.surface = surface
        if protection is None:
            raise Exception("Protection obligatoire")
        self.protection = protection
        # On attache la fenêtre au mur correspondant
        self.mur.fenetres.append(self)

class MurRideau(Mur, Fenetre):
    def __init__(self, orientation, surface, protection):
        Mur.__init__(self, orientation)
        Fenetre.__init__(self, self, surface, protection)

class Maison:
    def __init__(self, murs):
        self.murs = murs
        '''
            self.murNord  = murs[0]
            self.murOuest = murs[1]
            self.murSud   = murs[2]
            self.murEst   = murs[3]
        '''
    def surface_vitree(self):
        '''
            surfaceV = 0
            for mur in self.murs:
                for surface in mur.fenetres:
                    surfaceV += surface
            return surfaceV
        '''
        return sum(fen.surface for mur in self.murs for fen in mur.fenetres)

if __name__ == "__main__":
    # Instanciation des murs
    mur_nord  = Mur("Nord")
    mur_sud   = Mur("Sud")
    mur_est   = Mur("Est")
    mur_ouest = Mur("Ouest")

    # Instanciation des Fenetres
    fen_nord  = Fenetre(mur_nord, 0.5, "Store")
    fen_ouest = Fenetre(mur_ouest, 1, "Volet")
    fen_sud   = Fenetre(mur_sud, 2, "Volet")
    fen_est   = Fenetre(mur_est, 1, "Volet")

    # instanciation de la Maison avec les 4 murs
    maison = Maison([mur_nord, mur_ouest, mur_sud, mur_est])
    maison.murs[2] = MurRideau("Sud", 10, "Store")
    print(maison.surface_vitree())
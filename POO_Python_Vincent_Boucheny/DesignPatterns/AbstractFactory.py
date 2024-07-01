from enum import Enum  


# Une classe enumeration
class Nature(Enum):
    ALIMENTAIRE = 1
    SERVICE     = 2

class Produit:
    def __init__(self, nature):
        self.prix = 100
        self.nature = nature

class Facture:
    def __init__(self, produit, tva):
        self.produit = produit
        self.tva = tva/100
    def facturer(self):
        return self.produit.prix * (1 + self.tva)

class FactoryFacture
    def creer(produit):
        if produit.nature == Nature.ALIMENTAIRE:
            return Facture(produit, 5.5)
        elif produit.nature == Nature.SERVICE:
            return Facture(produit, 20)



if __name__ == "__main__":
    produit  = Produit(Nature.ALIMENTAIRE)
    prix_ttc = FactoryFacture.creer(produit).facturer()
    print(prix_ttc)
    
    produit  = Produit(Nature.SERVICE)
    prix_ttc = FactoryFacture.creer(produit).facturer()
    print(prix_ttc)
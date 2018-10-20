class Hero:
# constructeur
    def __init__(self):
        self.nom = ""
        self.pvMax = 20
        self.pvActu = self.pvMax
        self.atk = 5
        self.deff = 3
        self.gold = 20

    def _get_nom(self):
        return self.nom
    def _set_nom(self,leNom):
        self.nom=leNom

    def _get_pvMax(self):
        return self.pvMax
    def _set_pvActuel(self,nbHP):
        self.pvMax = nbHP

    def _get_pvActuel(self):
        return self.pvActu
    def _set_pvActuel(self,nbHP):
        self.pvActu = nbHP

    def _get_atk(self):
        return self.atk
    def _set_atk(self,nbAtk):
        self.pvActu = nbAtk

    def _get_deff(self):
        return self.deff
    def _set_deff(self,nbDeff):
        self.pvActu = nbDeff

    def _set_gold(self,nbPo):
        self.gold = nbPo
    def _get_gold(self):
        return self.gold


    def afficherBourse(self):
        return "Bourse Actuelle: %i pépins"%self.gold

    def afficherStats(self):
        return "%s PV %i/%i ATK: %i DEFF: %i Bourse: %i "%(self.nom,self.pvActu,self.pvMax,self.atk,self.deff,self.gold)

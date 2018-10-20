class Monstre:
    def __init__(self,leNom,lesPV,nbAtk,nbDeff,NbPoLoot):
        self.nom = leNom
        self.pvMax = lesPV
        self.pvActu = lesPV
        self.atk = nbAtk
        self.deff = nbDeff
        self.gold = NbPoLoot

    def _get_nom(self):
        return self.nom
    def _get_pvActu(self):
        return self.pvActu
    def _get_pvMax(self):
        return self.pvMax
    def _get_atk(self):
        return self.atk
    def _get_deff(self):
        return self.deff
    def _get_gold(self):
        return self.po

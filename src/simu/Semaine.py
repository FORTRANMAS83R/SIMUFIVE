import matplotlib.pyplot as plt
class Semaine:
    def __init__(self):
        self.five=None
        self.beach=None
        self.padel=None
        self.bar = None
        self.revenus = 0
        self.repartition = {
            "Five": 0,
            "Beach": 0,
            "Padel": 0,
            "Bar": 0
        }
    def calcul_repartition(self):
        tot = self.five.revenu + self.beach.revenu + self.padel.revenu + self.bar.revenus
        self.repartition["Five"] = self.five.revenu / tot
        self.repartition["Beach"] = self.beach.revenu / tot
        self.repartition["Padel"] = self.padel.revenu / tot
        self.repartition["Bar"] = self.bar.revenus / tot 

    def add(self,five,beach,padel, bar):
        self.five=five
        self.beach=beach
        self.padel=padel
        self.bar = bar
        self.calcul_repartition()
    
    def __str__(self):
        return "Résumé: \n\tRésultats:"+self.revenus+"\n\tRépartition: "+self.repartition+"\n"



        




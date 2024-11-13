import matplotlib.pyplot as plt
import Sport as sp 
import Bar as bar
class Semaine:
    def __init__(self):
        self.five= sp.Sport()
        self.beach=sp.Sport()
        self.padel= sp.Sport()
        self.bar = bar.Bar()
        self.revenus = 0
        self.repartition = {
            "Five": 0,
            "Beach": 0,
            "Padel": 0,
            "Bar": 0
        }
    def mean(self, semaines): 
        self.five.revenu = sum([semaine.five.revenu for semaine in semaines])/len(semaines)
        self.beach.revenu = sum([semaine.beach.revenu for semaine in semaines])/len(semaines)
        self.padel.revenu = sum([semaine.padel.revenu for semaine in semaines])/len(semaines)
        self.bar.revenus = sum([semaine.bar.revenus for semaine in semaines])/len(semaines)
        self.calcul_repartition()
        self.revenus = sum([semaine.revenus for semaine in semaines])/len(semaines)
        self.five.freq.res_hc = sum([semaine.five.freq.res_hc for semaine in semaines])/len(semaines)
        self.five.freq.res_hp = sum([semaine.five.freq.res_hp for semaine in semaines])/len(semaines)
        self.padel.freq.res_hc = sum([semaine.padel.freq.res_hc for semaine in semaines])/len(semaines)
        self.padel.freq.res_hp = sum([semaine.padel.freq.res_hp for semaine in semaines])/len(semaines)
        self.beach.freq.res_hc = sum([semaine.beach.freq.res_hc for semaine in semaines])/len(semaines)
        self.beach.freq.res_hp = sum([semaine.beach.freq.res_hp for semaine in semaines])/len(semaines)
        self.bar.affluence = sum([semaine.bar.affluence for semaine in semaines])/len(semaines)
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
        self.revenus = five.revenu + beach.revenu + padel.revenu + bar.revenus
    
    def __str__(self):
        return "Résumé: \n\tRésultats:"+str(self.revenus)+"\n\tRépartition: "+str(self.repartition)+"\n"



        




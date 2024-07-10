import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)

import config.cfg as cfg 
def init_amortissement():
    return cfg.amortissement

#calcul de l'amortissement mensuel linéaire
def calcul_amortissement(amortissement):
    for key in amortissement:
        amortissement[key]["valeur"] = amortissement[key]["valeur"] - amortissement[key]["valeur"]/(amortissement[key]["nb_annees"]*12)
    return amortissement

def total_amortissement(amortissement):
    total = 0
    for key in amortissement:
        total = total + amortissement[key]["valeur"]
    return total
"""
class Amortissement:
    def __init__(self,cle,val):
        self.nb_annees = cle
        self.valeur = val
    def get_nb_annees(self):
        return self.nb_annees
    def get_valeur(self):
        return self.valeur

class Amortissements:
    def __init__(self):
        self.amortissments=[]
    def get_amortissements(self):
        return self.amortissments
    def add_amortissement(self,amortissement):
        self.amortissments.append(amortissement)
    def to_
"""
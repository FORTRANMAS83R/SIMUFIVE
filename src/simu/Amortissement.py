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
        amortissement[key]["valeur"] = amortissement[key]["valeur"] - amortissement[key]["val_amortissement"]
    return amortissement

def total_amortissement(amortissement):
    total = 0
    for key in amortissement:
        total = total + amortissement[key]["valeur"]
    return total

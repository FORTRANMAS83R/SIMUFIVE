import sys
import os

# Ajouter le répertoire parent à sys.path
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
if parent_directory not in sys.path:
    sys.path.append(parent_directory)
import src.config.config as config
from src.simu.Frequentation import Frequentation
class Sport:
    def __init__(self, config): 
    
        self.freq = Frequentation(config.freq)
        self.nb_terrains = config.nb_terrains
        self.prix_hc = config.prix_hc
        self.prix_hp = config.prix_hp
        self.revenu = 0
    
    def evolve(self, i): 
        self.freq.evolve(i)
        self.revenu = self.freq.get_hc() * self.nb_terrains * self.prix_hc + self.freq.get_hp() * self.nb_terrains * self.prix_hp
    
    def get_revenu(self):
        return self.revenu
    
    def get_freq(self):
        return self.freq.to_dict()
    
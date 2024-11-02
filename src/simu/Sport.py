import sys
import os


# Ajouter le répertoire parent à sys.path
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
if parent_directory not in sys.path:
    sys.path.append(parent_directory)
import src.config.config as config
import src.config.param as param
from src.simu.Frequentation import Frequentation
class Sport:
    def __init__(self): 
        self.freq = Frequentation()
        self.nb_terrains = None
        self.prix_hc = None
        self.prix_hp = None
        self.revenu = 0
    def set_config(self, config): 
        self.freq.set_config(config.freq)
        self.nb_terrains = config.nb_terrains
        self.prix_hc = config.prix_hc
        self.prix_hp = config.prix_hp
        self.revenu = 0
    def set_without_config(self,freq_hc, freq_hp, revenu):
        self.freq.set_freq(freq_hc, freq_hp)
        self.revenu = revenu
    
    def evolve(self, i): 
        self.freq.evolve(i)
        self.revenu = self.freq.get_res_hc() * self.nb_terrains * self.prix_hc + self.freq.get_res_hp() * self.nb_terrains * self.prix_hp
    
    def clone(self):
        c = Sport()
        c.set_without_config(self.freq.get_hc(), self.freq.get_hp(), self.revenu)
        return c

        
    def get_revenu(self):
        return self.revenu
    
    def get_freq(self):
        return self.freq.to_dict()
    
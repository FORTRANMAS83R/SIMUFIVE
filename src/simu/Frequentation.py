import numpy as np
import math
import src.config.param as param
class Frequentation: 
    def __init__(self):
        self.freq_init_hc = None
        self.freq_max_hc = None
        self.var_hc = None
        self.type_evo_hc = None
        self.taux_evo_hc = None

        self.freq_init_hp = None
        self.freq_max_hp = None
        self.var_hp = None
        self.type_evo_hp = None
        self.taux_evo_hp = None

        self.freq_hc = None
        self.freq_hp = None

        self.res_hc = None
        self.res_hp = None
    def set_config(self, config): 
        self.freq_init_hc = config.freq_init_hc
        self.freq_max_hc = config.freq_max_hc
        self.var_hc = config.var_hc
        self.type_evo_hc = config.type_evo_hc
        self.taux_evo_hc = config.taux_evo_hc

        self.freq_init_hp = config.freq_init_hp
        self.freq_max_hp = config.freq_max_hp
        self.var_hp = config.var_hp
        self.type_evo_hp = config.type_evo_hp
        self.taux_evo_hp = config.taux_evo_hp

        self.freq_hc = None
        self.freq_hp = None
        
    def set_freq(self, freq_hc, freq_hp): 
        self.freq_hc = freq_hc
        self.freq_hp = freq_hp

        self.res_hc = freq_hc * param.NB_HEURES_HC
        self.res_hp = freq_hp * param.NB_HEURES_HP

    
    def evolve(self, i): 
        #Evolution de la fréquentation en heure creuse
        if self.type_evo_hc == "lineaire": 
            moy_freq_hc = self.freq_init_hc + i * self.taux_evo_hc
        elif self.type_evo_hc == "exponentielle": 
            moy_freq_hc = math.exp(self.taux_evo_hc * i) + (self.freq_init_hc -1 )
        elif self.type_evo_hc == "logarithmique": 
            moy_freq_hc = self.freq_init_hc + self.taux_evo_hc * math.log(i + 1)
        elif self.type_evo == "quadratique":
            moy_freq_hc = self.freq_init_hc + self.taux_evo_hc * i**2
        if moy_freq_hc > self.freq_max_hc: 
            moy_freq_hc = self.freq_max_hc
        self.freq_hc = np.random.normal(moy_freq_hc, self.var_hc)
        if self.freq_hc < 0: 
            self.freq_hc = 0
        if self.freq_hc > self.freq_max_hc: 
            self.freq_hc = self.freq_max_hc
        self.res_hc = self.freq_hc * param.NB_HEURES_HC
        
        #Evolution de la fréquentation en heure pleine
        if self.type_evo_hp == "lineaire": 
            moy_freq_hp = self.freq_init_hp + i * self.taux_evo_hp
        elif self.type_evo == "exponentielle": 
            moy_freq_hp = math.exp(self.taux_evo_hp * i) + (self.freq_init_hp -1 )
        elif self.type_evo == "logarithmique": 
            moy_freq_hp = self.freq_init_hp + self.taux_evo_hp * math.log(i + 1)
        elif self.type_evo == "quadratique":
            moy_freq_hp = self.freq_init_hp + self.taux_evo_hp * i**2
        if moy_freq_hp > self.freq_max_hp:
            moy_freq_hp = self.freq_max_hp
        self.freq_hp = np.random.normal(moy_freq_hp, self.var_hp)
        if self.freq_hp < 0: 
            self.freq_hp = 0
        if self.freq_hp > self.freq_max_hp:
            self.freq_hp = self.freq_max_hp
        self.res_hp = self.freq_hp * param.NB_HEURES_HP
    
    """
        Getters
    """
    def get_hc(self):
        return self.freq_hc
    def get_hp(self):
        return self.freq_hp
    
    def get_res_hc(self):
        return self.res_hc
    def get_res_hp(self):
        return self.res_hp
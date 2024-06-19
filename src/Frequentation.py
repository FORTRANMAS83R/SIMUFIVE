"""
On détermine ici la répartition des activités sur les heures de fréquentations 
1. On détermine ensuite un nombre de créneaux anniversaires par semaine, un nombre bloqué. On décompte 
   donc les heures des heures totales. Les séminaires se feront sur devis.
2. On a un taux de remplissage heure creuse & heure pleine accessible sur .cfg, on les appliques sur les heures restantes.
3. On retourne les valeurs d'heures occupés en heures pleines, en heures creuses, ainsi que le nombre d'anniversaires et de séminaires 
"""
import config.config as cfg 
class Frequentation:
    def __init__(self, hp_rate, hc_rate, nb_anniversaires):
        self.hp = hp_rate*cfg.HP
        self.vacantHp = cfg.HP-self.hp
        self.hc = int((cfg.HC-nb_anniversaires*3)*hc_rate)
        self.vacantHc = cfg.HC-self.hc
        self.nbAnniversaires = nb_anniversaires
    def getHp(self):
        return self.hp
    def getHc(self):
        return self.hc
    def getVacantHp(self):
        return self.vacantHp
    def getVacantHc(self):
        return self.vacantHc
    #useful? 
    def getNbAnniv(self):
        return self.nb_anniversaires
        """
    def getVisitors(self):
        return (self.hp+(self.hc-self.nb_anniversaires*3))*(cfg.NB_BEACH+cfg.NB_FIVE+cfg.NB_PADEL)
    """
    def __str__(self):
        return "Frequentation:\n\tNombre d'heures pleines occupees:"+str(self.hp)+"\n\tNombre d'heures creuses occupees:"+str(self.hc)+"\n\tNombre d'heures vacantes:"+str(self.vacantHc+self.vacantHp)+" ("+str(self.vacantHc)+" heures creuses, "+str(self.vacantHp)+" heures pleines)"+"\n\tNombre d'anniversaires:"+str(self.nbAnniversaires)+"\n"
    
    


"""
On détermine ici la répartition des activités sur les heures de fréquentations 
1. On détermine ensuite un nombre de créneaux anniversaires par semaine, un nombre bloqué. On décompte 
   donc les heures des heures totales. Les séminaires se feront sur devis.
2. On a un taux de remplissage heure creuse & heure pleine accessible sur .cfg, on les appliques sur les heures restantes.
3. On retourne les valeurs d'heures occupés en heures pleines, en heures creuses, ainsi que le nombre d'anniversaires et de séminaires 
"""
import config.config as cfg 
import pandas as pd

def meanFreq(Lfreq):
    hc=0
    hp=0
    nbanniv=0
    for freq in Lfreq:
        hc+=freq.getHc()
        hp+=freq.getHp()
        nbanniv+=freq.getNbAnniv()
    hc=hc/len(Lfreq)
    hp=hp/len(Lfreq)
    nbanniv=int(nbanniv/len(Lfreq))
    return Frequentation(hp,hc,nbanniv)
    #problème: le hp & hc ne sont pas des rates 


class Frequentation:
    def __init__(self, hp_rate, hc_rate, nb_anniversaires):
        if(hp_rate <1 and hc_rate <1):
            self.hp = round(hp_rate*cfg.HP,1)
            self.vacantHp = round(cfg.HP-self.hp,1)
            self.hc = round(int((cfg.HC-nb_anniversaires*3)*hc_rate),1)
            self.vacantHc = round(cfg.HC-self.hc,1)
            self.nbAnniversaires = nb_anniversaires
        else:
            self.hp = round(hp_rate,1)
            self.vacantHp = round(cfg.HP-self.hp,1)
            self.hc = round(hc_rate-nb_anniversaires*3,1)
            self.vacantHc = round(cfg.HC-self.hc,1)
            self.nbAnniversaires = nb_anniversaires
    def getHp(self):
        return self.hp
    def getHc(self):
        return self.hc
    def getVacantHp(self):
        return self.vacantHp
    def getVacantHc(self):
        return self.vacantHc
    def getTotal(self):
        return self.hc+self.hp
    #useful? 
    def getNbAnniv(self):
        return self.nbAnniversaires
        """
    def getVisitors(self):
        return (self.hp+(self.hc-self.nb_anniversaires*3))*(cfg.NB_BEACH+cfg.NB_FIVE+cfg.NB_PADEL)
    """
    def __str__(self):
        return "Frequentation:\n\tNombre d'heures pleines occupees:"+str(self.hp)+"\n\tNombre d'heures creuses occupees:"+str(self.hc)+"\n\tNombre d'heures vacantes:"+str(round(self.vacantHc+self.vacantHp,1))+" ("+str(self.vacantHc)+" heures creuses, "+str(self.vacantHp)+" heures pleines)"+"\n\tNombre d'anniversaires:"+str(self.nbAnniversaires)+"\n"
    
    def toDict(self,d):
        if not ("Frequentation" in d):
            d["Frequentation"]={}
            d["Frequentation"]["HP"]=[self.hp]
            d["Frequentation"]["HC"]=[self.hc]
            d["Frequentation"]["VacantHP"]=[self.vacantHp]
            d["Frequentation"]["VacantHC"]=[self.vacantHc]
            d["Frequentation"]["Anniversaires"]=[int(self.nbAnniversaires)+1]
        else:
            d["Frequentation"]["HP"].append(self.hp)
            d["Frequentation"]["HC"].append(self.hc)
            d["Frequentation"]["VacantHP"].append(self.vacantHp)
            d["Frequentation"]["VacantHC"].append(self.vacantHc)
            d["Frequentation"]["Anniversaires"].append(self.nbAnniversaires)
        return d["Frequentation"]
        



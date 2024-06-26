#idée ! une semaine aurait un attribut previous: permet d'avoir un comparateur avec la semaine précédente
# Créer un comparateur avec deux semaines ou plus ? 
import Revenue as rev
import Frequentation as freq
import config.config as cfg
import Charges as chg
import Date as d
import pandas as pd
class Semaine:
    def __init__(self,frequentation,abo,revenus,charges,date):
        self.frequentation=frequentation
        self.revenus=revenus
        self.totalRevenus=self.revenus.getTotal()
        self.charges=charges
        self.totalCharges=self.charges.totalCharges()
        self.abo=abo
        self.date=date
        self.resultat=self.revenus.getTotal()-self.charges.totalCharges()
    def getFrequentation(self):
        return self.frequentation
    def getRevenus(self):
        return self.revenus
    def getCharges(self):
        return self.charges
    def getAbo(self):
        return self.abo
    def getResultat(self):
        return self.resultat
    def getDate(self):
        return self.date
    def toDataFrame(self):
        return [self.date.toDataFrame(),self.frequentation.toDataFrame(),self.revenus.toDataFrame(),self.charges.toDataFrame(),self.abo.toDataFrame()]
    """
    def manqueAGagner(self):
        return(cfg.HC-self.frequentation.getHc)
    """
    def __str__(self):
        return str(self.date)+"\tNombre d'abonnes:"+str(self.abo.getNbSubs())+"\n"+str(self.revenus)+str(self.charges)+"\nResultat de la semaine:"+str(self.revenus.totalRevenu()-self.charges.totalCharges())+"\n"
       
class Semaines:
    def __init__(self):
        self.semaines=[]
    def addSemaine(self,semaine):
        self.semaines.append(semaine)
    def getSemaines(self):
        return self.semaines
    def toDict(self):
        s=dict()
        for i in range(len(self.semaines)):
            s["Semaine"+str(i)]=self.semaines[i].toDict()
        return s

    def __str__(self):
        c="Semaines: \n"
        for i in self.semaines:
            c+="\t"+str(i)+"\n"
        return c
    def toDict(self):
        d=dict()
        for semaine in self.semaines:
            d["Frequentation"]=semaine.getFrequentation().toDict(d)
            d["Revenus"]=semaine.getRevenus().toDict(d)
            if("Total revenus" in d):
                d["Total revenus"][""].append(semaine.getRevenus().getTotal())
            else:
                d["Total revenus"]={"":[semaine.getRevenus().getTotal()]}

            d["Charges"]=semaine.getCharges().toDict(d)
            if("Total charges" in d):
                d["Total charges"][""].append(semaine.getCharges().totalCharges())
            else:
                d["Total charges"]={"":[semaine.getCharges().totalCharges()]}
            if("Resultat" in d):
                d["Resultat"][""].append(semaine.getResultat())
            else:
                d["Resultat"]={"":[semaine.getResultat()]}
            """
            if("Abonnes" in d):
                d["Abonnes"].append(semaine.getAbo().getNbSubs())
            else:
                d["Abonnes"]=[semaine.getAbo().getNbSubs()]
                """
        return d


import pandas as pd

# Flatten the nested dictionary and create a DataFrame 


# Set MultiIndex 


# Display the resulting DataFrame 



        





"""
#Test
#Création de revennus 
rev1=rev.Revenu("Revenus Five",3000)
rev2=rev.Revenu("Revenus Beach",4000)
rev3=rev.Revenu("Revenus Padel",5000)
#Création de charges
charge1=chg.Charge("Electricité",1000)
charge2=chg.Charge("Eau",2000)
charge3=chg.Charge("Croquette",3000)

#Création de fréquentation
freq=freq.Frequentation(0.9,0.1,3)

charges =chg.Charges()
charges.addChargeF(charge1)
charges.addChargeF(charge2)
charges.addChargeV(charge3)

revennus = rev.Revenus()
revennus.addRevenu(rev1)
revennus.addRevenu(rev2)
revennus.addRevenu(rev3)

date = d.Date(1,1)

sem = Semaine(cfg.NB_SUBSCRIBERS,freq,revennus,charges,date)
print(str(sem))
"""
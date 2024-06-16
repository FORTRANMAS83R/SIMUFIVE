#idée ! une semaine aurait un attribut previous: permet d'avoir un comparateur avec la semaine précédente
# Créer un comparateur avec deux semaines ou plus ? 
import Revenue as rev
import Frequentation as freq
import config.config as cfg
import charges as chg
import Date as d
class Semaine:
    def __init__(self,nbSub,frequentation,revenus,charges,date):
        self.frequentation= frequentation
        self.revenus=revenus
        self.charges=charges
        self.nbSub=nbSub
        self.date=date
    def getRevenus(self):
        return self.revenus
    def getCharges(self):
        return self.charges
    def getFrequentation(self):
        return self.frequentation
    def manqueAGagner(self):
        return(cfg.HC-self.frequentation.getHc)*
    def __str__(self):
        return str(self.date)+str(self.frequentation)+"\tNombre d'abonnes:"+str(self.nbSub)+"\n"+str(self.revenus)+str(self.charges)+"\nResultat de la semaine:"+str(self.revenus.totalRevenu()-self.charges.totalCharges())
       
class Semaines:
    def __init__(self):
        self.semaines=[]
    def addSemaine(self,semaine):
        self.semaines.append(semaine)
    def getSemaines(self):
        return self.semaines
    def __str__(self):
        c="Semaines: \n"
        for i in self.semaines:
            c+="\t"+i.toString()+"\n"
        return c

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
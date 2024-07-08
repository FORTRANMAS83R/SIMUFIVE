import simu.Frequentation as freq
import simu.Transaction as Transaction
import config.cfg as cfg 
import simu.Abonnements as ab
import pandas as pd

#Méthodes de calcul des revenus par activité
def revenueFivePrivate(freq):
    return(freq.getHc()*cfg.HC_PRICE_FIVE+freq.getHp()*cfg.HP_PRICE_FIVE)
def revenueBeachPrivate(freq):
    return(freq.getHc()*cfg.HC_PRICE_BEACH+freq.getHp()*cfg.HP_PRICE_BEACH)
def revenuePadelPrivate(freq):
    return(freq.getHc()*cfg.HC_PRICE_PADEL+freq.getHp()*cfg.HP_PRICE_PADEL)
def revenueAnnivPrivate(freq):
    return(freq.getNbAnniv()*cfg.PRICE_ANNIV)
#CLASSE A FACTORISER AVEC @CHARgE
class Revenu(Transaction.Transaction):
    def __init__(self,cle,val):
        Transaction.Transaction.__init__(self,cle,val)

class Revenus : 

    def __init__(self):
        self.revenus=[]
    def addRevenu(self,revenu):
        self.revenus.append(revenu)
    def getRevenus(self):
        return self.revenus
    def modifyRevenu(self,cle,val):
        for i in self.revenus:
            if i==cle:
                self.revenus[i]=val
    def getRevenu(self,cle):
        for i in self.revenus:
            if i.cle==cle:
                return i.val
        return None
    def getTotal(self):
        s=0
        for i in self.revenus:
            s+=i.getVal()
        return s
    def __str__(self):
        c="Revenus: \n"
        for i in self.revenus:
            c+="\t"+str(i)+"\n"
        return c
    def toDict(self,d):
        if not ("Revenus" in d):
            d["Revenus"]={}
            for rev in self.revenus:
                d["Revenus"][rev.getCle()]=[rev.getVal()]
        else:
            for rev in self.revenus:
                d["Revenus"][rev.getCle()].append(rev.getVal())
        return d["Revenus"]

    #getter   
    def getRevenus(self):
        return self.revenus
    def getRevenu(self,cle):
        for i in self.revenus:
            if i.cle==cle:
                return i.val
        return None
    


    










    
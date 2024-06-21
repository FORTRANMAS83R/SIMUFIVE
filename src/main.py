import IHM 
import config.config as cfg
import Semaine 
import Charges
import Frequentation
import Revenue
import Five 
import Beach
import Padel
import Bar 
import Date 
import MiseEnForme as mf
import random as rd 
import Abonnements as ab 


def applyDelta(delta):
    if(cfg.deltaActive):
        return rd.randrange(-delta,delta)
    return 0

#precFreq est un tuple contenant hc_rate & hp_rate 
def calculFreqLineaire(precFreq, evoFreq):
    return precFreq[0]+evoFreq-applyDelta(cfg.deltaFreq),precFreq[1]+evoFreq-applyDelta(cfg.deltaFreq)

def calculFreqAvecCreux(precFreq,loss,n):
    if(n<=0):
        return precFreq
    else:
        return precFreq[0]-loss-applyDelta(cfg.deltaFreq),precFreq[1]-loss-applyDelta(cfg.deltaFreq)
def toGlobal(dic):
    global config 
    config = dic 
def init(dic):
    i=mf.extendsDic(dic,'evoFreq')
    toGlobal(i)


def buildSimu(dic):
    init(dic)
    if(config["dureeSimu"]=="Semestre"):
        dureeSimu=6*4
    elif(config["dureeSimu"]=="Annee"):
        dureeSimu=12*4
    elif(config["dureeSimu"]=="Trimestre"):
        dureeSimu=3*4
    else:
        dureeSimu=3*4*12
    semaines =Semaine.Semaines()
    abo=ab.Abonnements()
    for i in range(1,dureeSimu+1):
        charges = Charges.Charges()
        revenus = Revenue.Revenus()
        #Détermination de la fréquentation des sports 
        if(config["TypeEvo"]=="lineaire"):
            if(i==1):
                freqFive=(config["freqInitFive"]-rd.randrange(-10,20),config["freqInitFive"])
                freqBeach=(config["freqInitBeach"]-rd.randrange(-10,20),config["freqInitBeach"])
                freqPadel=(config["freqInitPadel"]-rd.randrange(-10,20),config["freqInitPadel"])
            else:
                freqFive,freqBeach,freqPadel=calculFreqLineaire(freqFive,config["tauxAugmentation"]),calculFreqLineaire(freqBeach,config["tauxAugmentation"]),calculFreqLineaire(freqPadel,config["tauxAugmentation"])
        else:
            if(i==1):
                freqFive=(config["freqInitFive"]-rd.randrange(-10,20),config["freqInitFive"])
                freqBeach=(config["freqInitBeach"]-rd.randrange(-10,20),config["freqInitBeach"])
                freqPadel=(config["freqInitPadel"]-rd.randrange(-10,20),config["freqInitPadel"])
            else:
                freqFive,freqBeach,freqPadel=calculFreqAvecCreux(freqFive,config["tauxBaisse"],config["duree"]+1-i),calculFreqAvecCreux(freqBeach,config["tauxBaisse"],config["duree"]+1-i),calculFreqAvecCreux(freqPadel,config["tauxBaisse"],config["duree"]+1-i)
        #Création des frequentations des sports 
        freq_Five = Frequentation.Frequentation(freqFive[1]/100,freqFive[0]/100,rd.randint(0,cfg.deltaNbAnniv))
        freq_Beach=Frequentation.Frequentation(freqBeach[1]/100,freqBeach[0]/100,rd.randint(0,cfg.deltaNbAnniv))
        freq_Padel=Frequentation.Frequentation(freqPadel[1]/100,freqPadel[0]/100,rd.randint(0,cfg.deltaNbAnniv))

        #Création des objets sports 
        five = Five.Five(freq_Five)
        beach=Beach.Beach(freq_Beach)
        padel=Padel.Padel(freq_Padel)
        #Création objet Bar 
        bar = Bar.Bar(Bar.getNbVisit(five,beach,padel,config["freqBar"]/100),config["ticketMoyenBar"],config["margeBar"]/100)


        #Création des revennus sport
        revenus.addRevenu(Revenue.Revenu("Five",five.getRevenu()))
        revenus.addRevenu(Revenue.Revenu("Beach",beach.getRevenu()))
        revenus.addRevenu(Revenue.Revenu("Padel",padel.getRevenu()))
        #Création revennus bar 
        revenus.addRevenu(Revenue.Revenu("Bar",bar.getRevenu()))

        #Les abbonnés ne payant pas leur partie 
        revenus.addRevenu(Revenue.Revenu("Abo loss",-abo.getLoss()))

        #Charges hebdomadaires 
        charges.addChargeV(Charges.Charge("Conso bar",bar.getCharges()))
        charges.addChargeV(Charges.Charge("IS",revenus.totalRevenu()*0.25))
            
        if(i%4==0):
            for c in cfg.chargesExit:
                charges.addChargeF(Charges.Charge(c,float(cfg.chargesExit[c])))
            #Abonnements
            revenus.addRevenu(Revenue.Revenu("Abonnements",abo.getRevenu()))
            #Ajout des charges mensuelles 
        if(i%12==0):
            u=2
        semaines.addSemaine(Semaine.Semaine(abo,revenus,charges,Date.Date(i,int(i/12))))
        abo.varSubs(applyDelta(cfg.deltaSub))
    print(str(semaines))

            #Ajout des charges annuelles & des impots 

        #Management des revennus et dépenses du bar 
        #Création des revennus sports 
        #Création de la semaine et ajout à semaine 
    #Réaliser un toString 

    
        
buildSimu(cfg.configExit)
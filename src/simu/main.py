#import IHM 
import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))

parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)
import simu.Semaine as Semaine
import simu.Charges as Charges
import simu.Frequentation as Frequentation
import simu.Revenue as Revenue
import simu.Five as Five 
import simu.Beach as Beach
import simu.Padel as Padel
import simu.Bar as Bar 
import simu.Date as Date 
import simu.MiseEnForme as mf
import random as rd 
import simu.Abonnements as ab 
import simu.Amortissement as am





import config.cfg as cfg
import config.config as param




def applyDelta(delta):
    if(param.deltaActive==True):
        return rd.randrange(-delta,delta)/100
    return 0
def applyAnniv(sport):
    if(cfg.config[sport]["anniv_active"]==True):
        return rd.randrange(0,param.deltaNbAnniv)
    return 0

#precFreq est un tuple contenant hc_rate & hp_rate 
def calculFreqLineaire(precFreq, evoFreq):
    if(precFreq[0]>=param.freqPlafond):
        precFreq=param.freqPlafond,precFreq[1]+evoFreq-applyDelta(param.deltaFreq)
    if( precFreq[1]>=param.freqPlafond):
        precFreq=precFreq[0]+evoFreq-applyDelta(param.deltaFreq),param.freqPlafond
    else:
        precFreq=precFreq[0]+evoFreq-applyDelta(param.deltaFreq),precFreq[1]+evoFreq-applyDelta(param.deltaFreq)
    return precFreq
    


def calculFreqAvecCreux(precFreq,loss,n):
    if(n<=0):
        return precFreq[0]-applyDelta(cfg.deltaFreq),precFreq[1]-applyDelta(cfg.deltaFreq)
    else:
        return precFreq[0]-loss-applyDelta(cfg.deltaFreq),precFreq[1]-loss-applyDelta(cfg.deltaFreq)
def toGlobal(dic):
    #global cfg.config 
    cfg.config = dic 
def init(dic):
    i=mf.extendsDic(dic,'evoFreq')
    toGlobal(i)


def buildSimu():
    current_amo=am.init_amortissement()
    #init(dic)
    if(cfg.config["duree_simu"]=="Semestre"):
        dureeSimu=6*4
    elif(cfg.config["duree_simu"]=="Annee"):
        dureeSimu=12*4
    elif(cfg.config["duree_simu"]=="Trimestre"):
        dureeSimu=3*4
    else:
        dureeSimu=3*4*12
    semaines =Semaine.Semaines()
    abo=ab.Abonnements()
    for i in range(1,dureeSimu+1):
        charges = Charges.Charges()
        revenus = Revenue.Revenus()
        #Détermination de la fréquentation des sports 
    
        if(i==1):
            freqFive=(cfg.config["Five"]["freq_init"]-rd.randrange(-10,20),cfg.config["Five"]["freq_init"])
            freqBeach=(cfg.config["Beach"]["freq_init"]-rd.randrange(-10,20),cfg.config["Beach"]["freq_init"])
            freqPadel=(cfg.config["Padel"]["freq_init"]-rd.randrange(-10,20),cfg.config["Padel"]["freq_init"])
        else:
                freqFive,freqBeach,freqPadel=calculFreqLineaire(freqFive,cfg.config["Five"]["evolution"]["taux_evolution"]),calculFreqLineaire(freqBeach,cfg.config["Beach"]["evolution"]["taux_evolution"]),calculFreqLineaire(freqPadel,cfg.config["Padel"]["evolution"]["taux_evolution"])
        #else:
        #    #Pas stable for now 
        #    if(i==1):
        #        freqFive=(cfg.config["freqInitFive"]-rd.randrange(-10,20),cfg.config["freqInitFive"])
        #        freqBeach=(cfg.config["freqInitBeach"]-rd.randrange(-10,20),cfg.config["freqInitBeach"])
        #        freqPadel=(cfg.config["freqInitPadel"]-rd.randrange(-10,20),cfg.config["freqInitPadel"])
        #    else:
        #        freqFive,freqBeach,freqPadel=calculFreqAvecCreux(freqFive,cfg.config["tauxBaisse"],cfg.config["duree"]+1-i),calculFreqAvecCreux(freqBeach,cfg.config["tauxBaisse"],cfg.config["duree"]+1-i),calculFreqAvecCreux(freqPadel,cfg.config["tauxBaisse"],cfg.config["duree"]+1-i)
        #Création des frequentations des sports 
        freq_Five = Frequentation.Frequentation(freqFive[1]/100,freqFive[0]/100,applyAnniv("Five"))
        freq_Beach=Frequentation.Frequentation(freqBeach[1]/100,freqBeach[0]/100,applyAnniv("Beach"))
        freq_Padel=Frequentation.Frequentation(freqPadel[1]/100,freqPadel[0]/100,applyAnniv("Padel"))
        meanFreq = Frequentation.meanFreq([freq_Five,freq_Beach,freq_Padel])

        #Création des objets sports 
        five = Five.Five(freq_Five)
        beach=Beach.Beach(freq_Beach)
        padel=Padel.Padel(freq_Padel)

        #Création objet Bar 
        bar = Bar.Bar(Bar.getNbVisit(five,beach,padel,cfg.config["Bar"]["taux_freq"]/100)+(cfg.config["Bar"]["freq_add"]/100),cfg.config["Bar"]["ticket_moyen"],cfg.config["Bar"]["marge"]/100)


        #Création des revennus sport
        revenus.addRevenu(Revenue.Revenu("Five",five.getRevenu()))
        revenus.addRevenu(Revenue.Revenu("Beach",beach.getRevenu()))
        revenus.addRevenu(Revenue.Revenu("Padel",padel.getRevenu()))
        #Création revennus bar 
        revenus.addRevenu(Revenue.Revenu("Bar",bar.getRevenu()))
        
        #Charges hebdomadaires 
        charges.addChargeV(Charges.Charge("Conso bar",bar.getCharges()))
        #charges.addChargeV(Charges.Charge("IS",revenus.getTotal()*0.25))
        charges.addChargeV(Charges.Charge("TVA",revenus.getTotal()*0.2))

            
        if(i%4==0):
            for c in cfg.config["charges"]:
                charges.addChargeF(Charges.Charge(c,float(cfg.config["charges"][c])))
            #Abonnements & events
            revenus.addRevenu(Revenue.Revenu("Abonnements",abo.getRevenu()))
            revenus.addRevenu(Revenue.Revenu("Evenement Club House",bar.getNbVisit()/7*param.AUGMENTATION_EVENT_BAR/100*param.TICKET_MEAN_BAR_EVENT))
            for cle in current_amo:
                charges.addChargeF(Charges.Charge(cle,current_amo[cle]["val_amortissement"]))
        else: 
            for c in cfg.config["charges"]:
                charges.addChargeF(Charges.Charge(c,0))
            revenus.addRevenu(Revenue.Revenu("Abonnements",0))
            revenus.addRevenu(Revenue.Revenu("Evenement Club House",0))
            for cle in current_amo:
                charges.addChargeF(Charges.Charge(cle,0))
         #Les abbonnés ne payant pas leur partie 
        #revenus.addRevenu(Revenue.Revenu("Abo loss",-abo.getLoss()))

        charges.addChargeV(Charges.Charge("Communication",revenus.getTotal()*param.BUDGET_COM))
        semaines.addSemaine(Semaine.Semaine(meanFreq,abo,revenus,charges,Date.Date(i,int(i/12))))
        abo.varSubs(applyDelta(param.deltaSub))
        current_amo=am.calcul_amortissement(current_amo)
    return semaines.toDict()






buildSimu()
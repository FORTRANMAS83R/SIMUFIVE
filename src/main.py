import IHM 
import config.config as cfg
import Semaine 
import Charges
import Frequentation
import Revenue



def buildSimu(dureeSimu,freqInitFive,freqInitBeach,freqInitPadel,evoFreq,freqBar,ticketMoyenBar,margeBar):
    if(dureeSimu=="Semestre"):
        dureeSimu=6*4
    elif(dureeSimu=="Annee"):
        dureeSimu=12*4
    elif(dureeSimu=="Trimestre"):
        dureeSimu=3*4
    else:
        dureeSimu=3*4*12
    semaines =Semaine.Semaines()
    for i in range(1,dureeSimu+1):
        #Instanciation de charges & de revennus 
        if(i%4==0):
            u=1
            #Ajout des charges mensuelles 
        if(i==1 or i%12==0):
            u=2
            #Ajout des charges annuelles & des impots 

        #Management des revennus et dépenses du bar 
        #Création des revennus sports 
        #Création de la semaine et ajout à semaine 
    #Réaliser un toString 

    
        

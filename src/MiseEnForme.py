import config.config as cfg 
def miseEnFormeEvoFreq(evoFreq):
    ev=evoFreq.split(", ")
    toR={"TypeEvo":ev[0]}
    for i in range(1,len(ev)):
        tA=ev[i].split(": ")
        toR[tA[0]]=float(tA[1])
    return toR
        

B={'dureeSimu': 'Semestre', 'freqInitFive': 4.0, 'freqInitBeach': 4.0, 'freqInitPadel': 4.0, 'evoFreq': 'creu, duree: 4, tauxBaisse: 4.0', 'freqBar': 4.0, 'ticketMoyenBar': 4.0, 'margeBar': 4.0}

def extendsDic(dic,cle):
    el=miseEnFormeEvoFreq(dic[cle])
    dic.pop(cle)
    for cle in el:
        dic[cle]=el[cle]
    return dic


 

#print(extendsDic(B,'evoFreq'))
"""
class dict(dict):
    def extends(self,cle):
        el=miseEnFormeEvoFreq(self[cle])
        self.pop(cle)
        for cle in el:
            self[cle]=el[cle]
        return self
print(B)
B.extends('evoFreq')
print(B)
"""

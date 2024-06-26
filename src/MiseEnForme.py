import config.config as cfg 
def miseEnFormeEvoFreq(evoFreq):
    ev=evoFreq.split(", ")
    toR={"TypeEvo":ev[0]}
    for i in range(1,len(ev)):
        tA=ev[i].split(": ")
        toR[tA[0]]=float(tA[1])
    return toR
        
def extendsDic(dic,cle):
    el=miseEnFormeEvoFreq(dic[cle])
    dic.pop(cle)
    for cle in el:
        dic[cle]=el[cle]
    return dic


 


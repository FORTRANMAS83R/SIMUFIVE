import config.cfg as cfg 
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


import numpy as np

def modele_frequentation(heure, jour):
    # Heures de pointe en semaine
    heures_semaine = [17, 18, 19, 20, 21]
    # Heures de pointe le week-end
    heures_weekend = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    if jour in ['samedi', 'dimanche']:
        if heure in heures_weekend:
            return np.random.poisson(lam=50)  # Lamda est le nombre moyen de visiteurs
        else:
            return np.random.poisson(lam=20)
    else:
        if heure in heures_semaine:
            return np.random.poisson(lam=40)
        else:
            return np.random.poisson(lam=10)

# Exemple d'utilisation
jour = 'vendredi'
heure = 20
print(f"Fréquentation estimée pour {jour} à {heure}h : {modele_frequentation(heure, jour)} visiteurs")


import matplotlib.pyplot as plt
import numpy as np
import Semaine as s
"""
Une fonction qui affiche l'évolution de hp_rate et hc_rate dans un objet semaines de type Semaines
"""
def plotFreq(semaines):
    semaines = semaines.getSemaines()
    x = np.arange(len(semaines))
    y1 = [i.hp_rate for i in semaines]
    y2 = [i.hc_rate for i in semaines]
    plt.plot(x, y1, label='hp_rate')
    plt.plot(x, y2, label='hc_rate')
    plt.legend()
    plt.show()


#Tests
#On crée une semaine
import random as rd
import Charges as chg
import Frequentation as freq
import Revenus as rev
for(i=1;i<=52;i++):
    # arandom float between 0 and 1
    hp_rate = rd.random(0,1)
    hc_rate =rd.random(0,1)
    nb_anniversaires = rd.randint(0,5)
    f = s.Frequentation(hp_rate,hc_rate,nb_anniversaires)
    r = s.Revenus()
    c = s.Charges()
    semaine = s.Semaine(0.5,0.5,0.5,f,r,c)
    semaines.addSemaine(semaine)
f = s.Frequentation(0.5,0.5,1)


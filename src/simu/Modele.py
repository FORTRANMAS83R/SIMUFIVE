import matplotlib.pyplot as plt
import numpy as np

class Simu: 
    def __init__(self):
        self.troncons = []
    def add_troncon(self, troncon):
        self.troncons.append(troncon)
class Troncon:
    def __init__(self,plage,creux):
        self.plage = plage
        self.creux = creux
class TronconLineaire(Troncon):
    def __init__(self,plage,creux,a,plafond):
        super().__init__(plage,creux)
        self.a = a
        self.plafond = plafond
    def calcul_frequentation(self):
        freq=[]
        for t in range(self.plage[0],self.plage[1]):
            if self.a*t<self.plafond:
                freq.append(float((self.a*t-self.plage[0])-self.creux))
            else:
                freq.append(float(self.plafond-self.creux))
        return freq
class TronconExponentiel(Troncon):
    def __init__(self,plage,creux,t_0,vMax,decr):
        super().__init__(plage,creux)
        self.vMax = vMax
        self.decr = decr
    def calcul_frequentation(self):
        freq=[]
        for t in range(self.plage[0],self.plage[1]):
            freq.append(float(self.vMax*np.exp(-self.decr*(t-self.plage[0]))-self.creux))
        return freq



s=Simu()
duree_simu = 100
liste=[]
troncon1 = TronconExponentiel([0,10],0,0,95,7).calcul_frequentation()
print(len(troncon1))
liste+=troncon1
troncon2 = TronconLineaire([10,20],0,10,95).calcul_frequentation()
print(len(troncon2))
liste+=troncon2
troncon3 = TronconLineaire([20,30],25,3,95).calcul_frequentation()
print(len(troncon3))
liste+=troncon3

t=np.arange(30)
plt.plot(t,liste)
plt.show()




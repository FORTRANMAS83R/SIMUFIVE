import matplotlib.pyplot as plt
class Semaine:
    def __init__(self):
        self.five=None
        self.beach=None
        self.padel=None
    def add(self,five,beach,padel):
        self.five=five
        self.beach=beach
        self.padel=padel
    
       
class Semaines:
    def __init__(self):
        self.semaines=[]
        self.CA = 0
    def add(self,semaine):
        self.semaines.append(semaine)
        self.CA+=semaine.five.revenu+semaine.beach.revenu+semaine.padel.revenu
    def compare(self):
        #Compléter, pourrait servir à comparer plusieurs simulaytions 
        return None
    def plot(self):
        n_semaine=[]
        res_five=[]
        res_beach=[]
        res_padel=[]
        CA=[]
        i=0
        for semaine in self.semaines:
            n_semaine.append(i)
            res_five.append(semaine.five.revenu)
            res_beach.append(semaine.beach.revenu)
            res_padel.append(semaine.padel.revenu)
            
            i+=1
        plt.plot(n_semaine,res_five,label="Five")
        plt.plot(n_semaine,res_beach,label="Beach")
        plt.plot(n_semaine,res_padel,label="Padel")
        plt.show()
            



        




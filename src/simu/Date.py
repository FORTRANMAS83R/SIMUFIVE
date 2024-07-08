import pandas as pd
class Date: 
    def __init__(self, numSemaine,numAnnee):
        self.numSemaine=numSemaine
        self.numAnnee=numAnnee
    def getNumSemaine(self):
        return self.numSemaine
    def getNumAnnee(self):
        return self.numAnnee
    def setNumSemaine(self,numSemaine):
        self.numSemaine=numSemaine
    def setNumAnnee(self,numAnnee):
        self.numAnnee=numAnnee
    def toDataFrame(self):
        return pd.DataFrame({"Semaine":[self.numSemaine],"Annee":[self.numAnnee]})
    def __str__(self):
        return "Semaine n° "+str(self.numSemaine)+" de l'année n° "+str(self.numAnnee)+":\n"
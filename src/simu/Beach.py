import config.config as param 
import simu.Frequentation as freq
import simu.Sport as Sport
class Beach(Sport.Sport): 
    
    def __init__(self,frequentation):
        Sport.Sport.__init__(self,frequentation)
        self.revenu=self.freq.getHc()*param.HC_PRICE_BEACH+self.freq.getHp()*param.HP_PRICE_BEACH+self.freq.getNbAnniv()*param.PRICE_ANNIV
        self.manqueAGagner = self.freq.getVacantHc()*param.HC_PRICE_BEACH+self.freq.getVacantHp()*param.HP_PRICE_BEACH
    def __str__(self):
        return "Beach:\n\t"+str(self.freq)+"\n\tRevenu:"+str(self.revenu)+"\n\tManque a gagner:"+str(self.manqueAGagner)+"\n"
    


import config.config as cfg 
import Frequentation as freq
import Sport
class Beach(Sport.Sport): 
    
    def __init__(self,frequentation):
        Sport.Sport.__init__(self,frequentation)
        self.revenu=self.freq.getHc()*cfg.HC_PRICE_BEACH+self.freq.getHp()*cfg.HP_PRICE_BEACH
        self.manqueAGagner = self.freq.getVacantHc()*cfg.HC_PRICE_BEACH+self.freq.getVacantHp()*cfg.HP_PRICE_BEACH
    def __str__(self):
        return "Beach:\n\t"+str(self.freq)+"\n\tRevenu:"+str(self.revenu)+"\n\tManque a gagner:"+str(self.manqueAGagner)+"\n"
    

freq = freq.Frequentation(0.8,0.6,2)
beach = Beach(freq)
print(beach.getRevenu())
print(beach.getManqueAGagner())
print(beach)
import config.config as cfg 
import Frequentation as freq
import Sport 
class Five(Sport.Sport): 
    def __init__(self,frequentation):
        Sport.Sport.__init__(self,frequentation)
        self.revenu=self.freq.getHc()*cfg.HC_PRICE_FIVE+self.freq.getHp()*cfg.HP_PRICE_FIVE+self.freq.getNbAnniv()*cfg.PRICE_ANNIV
        self.manqueAGagner = self.freq.getVacantHc()*cfg.HC_PRICE_FIVE+self.freq.getVacantHp()*cfg.HP_PRICE_FIVE
    
    def __str__(self):
        return "Five:\n\t"+str(self.freq)+"\n\tRevenu:"+str(self.revenu)+"\n\tManque a gagner:"+str(self.manqueAGagner)+"\n"


"""
frequ = freq.Frequentation(0.8,0.6,2)
five = Five(frequ)
print(five.getRevenu())
print(five.getManqueAGagner())
print(five)
"""
import config.config as param 
import simu.Frequentation as freq
import simu.Sport as Sport
class Five(Sport.Sport): 
    def __init__(self,frequentation):
        Sport.Sport.__init__(self,frequentation)
        self.revenu=self.freq.getHc()*param.HC_PRICE_FIVE+self.freq.getHp()*param.HP_PRICE_FIVE+self.freq.getNbAnniv()*param.PRICE_ANNIV
        self.manqueAGagner = self.freq.getVacantHc()*param.HC_PRICE_FIVE+self.freq.getVacantHp()*param.HP_PRICE_FIVE
    
    def __str__(self):
        return "Five:\n\t"+str(self.freq)+"\n\tRevenu:"+str(self.revenu)+"\n\tManque a gagner:"+str(self.manqueAGagner)+"\n"


"""
frequ = freq.Frequentation(0.8,0.6,2)
five = Five(frequ)
print(five.getRevenu())
print(five.getManqueAGagner())
print(five)
"""
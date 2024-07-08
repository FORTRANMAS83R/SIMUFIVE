import config.config as param 
import simu.Frequentation as freq
import simu.Sport as Sport
class Padel(Sport.Sport):
    def __init__(self,frequentation):
        Sport.Sport.__init__(self,frequentation)
        self.revenu=self.freq.getHc()*param.HC_PRICE_PADEL+self.freq.getHp()*param.HP_PRICE_PADEL+self.freq.getNbAnniv()*param.PRICE_ANNIV
        self.manqueAGagner = self.freq.getVacantHc()*param.HC_PRICE_PADEL+self.freq.getVacantHp()*param.HP_PRICE_PADEL

    def __str__(self):
        return "Padel:\n\t"+str(self.freq)+"\n\tRevenu:"+str(self.revenu)+"\n\tManque a gagner:"+str(self.manqueAGagner)+"\n"
        


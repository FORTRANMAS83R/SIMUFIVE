import config.config as cfg 
import Frequentation as freq
import Sport
class Padel(Sport.Sport):
    def __init__(self,frequentation):
        Sport.Sport.__init__(self,frequentation)
        self.revenu=self.freq.getHc()*cfg.HC_PRICE_PADEL+self.freq.getHp()*cfg.HP_PRICE_PADEL
        self.manqueAGagner = self.freq.getVacantHc()*cfg.HC_PRICE_PADEL+self.freq.getVacantHp()*cfg.HP_PRICE_PADEL

    def __str__(self):
        return "Padel:\n\t"+str(self.freq)+"\n\tRevenu:"+str(self.revenu)+"\n\tManque a gagner:"+str(self.manqueAGagner)+"\n"
        


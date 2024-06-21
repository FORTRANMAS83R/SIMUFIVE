
import config.config as cfg

class Abonnements:
    def __init__(self):
        self.nbSubs=cfg.NB_SUBSCRIBERS
        self.revenu=self.nbSubs*cfg.SUBSCRIPTION_PRICE #mensuel
        self.loss=self.nbSubs*((cfg.MEAN_PRICE_BEACH/cfg.NB_BEACH)+(cfg.MEAN_PRICE_FIVE/cfg.NB_FIVE)+(cfg.MEAN_PRICE_PADEL/cfg.NB_PADEL)) #annuel

    def varSubs(self,var):
        self.nbSubs=self.nbSubs+var
    def getRevenu(self):
        return self.revenu
    def getLoss(self):
        return self.loss
    def getNbSubs(self):
        return self.nbSubs
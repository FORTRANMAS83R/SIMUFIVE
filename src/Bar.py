
import config.config as cfg 
def chargesBar(meanTicket,nbOfVisitors,margin):
    return (margin-1)*revenueBar(meanTicket,nbOfVisitors)
def getNbVisit(Five,Beach,Padel,freqBar_rate):
    return (Five.getFrequentation().getTotal()*cfg.NB_FIVE*cfg.NB_PLAYER_FIVE+Beach.getFrequentation().getTotal()*cfg.NB_BEACH*cfg.NB_PLAYER_BEACH+Padel.getFrequentation().getTotal()*cfg.NB_PADEL*cfg.NB_PLAYER_PADEL)*freqBar_rate


class Bar: 
    def __init__(self,nbVisit,ticketMoyen,marge):
        self.nbVisit=nbVisit
        self.revenu=nbVisit*ticketMoyen
        self.charges=(nbVisit*ticketMoyen)/(1+marge)
    def getRevenu(self):
        return self.revenu
    def getCharges(self):
        return self.charges
    def getNbVisit(self):
        return self.nbVisit


b=Bar(8,8,0.7)
print(type(b.getCharges()))
    


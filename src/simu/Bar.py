
import config.config as param 
def chargesBar(meanTicket,nbOfVisitors,margin):
    return (margin-1)*revenueBar(meanTicket,nbOfVisitors)
def getNbVisit(Five,Beach,Padel,freqBar_rate):
    return (Five.getFrequentation().getTotal()*param.NB_FIVE*param.NB_PLAYER_FIVE+Beach.getFrequentation().getTotal()*param.NB_BEACH*param.NB_PLAYER_BEACH+Padel.getFrequentation().getTotal()*param.NB_PADEL*param.NB_PLAYER_PADEL)*freqBar_rate


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
    


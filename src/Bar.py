
def chargesBar(meanTicket,nbOfVisitors,margin):
    return (margin-1)*revenueBar(meanTicket,nbOfVisitors)
def getNbVisit(Five,Beach,Padel,freqBar_rate):
    return (Five.getFrequentation().getTotal()+Beach.getFrequentation().getTotal()+Padel.getFrequentation().getTotal())*freqBar_rate

class Bar: 
    def __init__(self,nbVisit,ticketMoyen,marge):
        self.revenu=nbVisit*ticketMoyen
        self.charges=(nbVisit*ticketMoyen)/(1+marge)
    def getRevenu(self):
        return self.revenu
    def getCharges(self):
        return self.charges


b=Bar(8,8,0.7)
print(type(b.getCharges()))
    


def revenueBar(meanTicket,nbOfVisitors):
    return meanTicket*nbOfVisitors
def chargesBar(meanTicket,nbOfVisitors,margin):
    return (margin-1)*revenueBar(meanTicket,nbOfVisitors)


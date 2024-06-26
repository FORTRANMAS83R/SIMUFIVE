class Transaction: 
    def __init__(self,cle,val):
        self.cle=cle
        self.val=val
    def getVal(self):
        return self.val
    def getCle(self):
        return self.cle
    def __str__(self):
        return(self.cle+": "+str(self.val))
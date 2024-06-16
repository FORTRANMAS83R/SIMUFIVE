
"""
Création d'un objet Charge & d'un objet Charges.
Charge:
    -une clé: le nom de la charge
    -une val: la valeur de la charge
Charges:
    -chargesF: une liste d'objets Charge, fixe 
    -chargesV: //, variable 
"""
import Transaction
class Charge(Transaction.Transaction):
    def __init__(self,cle,val):
        Transaction.Transaction.__init__(self,cle,val)

class Charges:
    def __init__(self):
        self.chargesF=[]
        self.chargesV=[]

    def addChargeF(self,charge):
        self.chargesF.append(charge)

    def addChargeV(self,charge):
        self.chargesV.append(charge)

    def totalChargesF(self):
        s=0
        for i in self.chargesF:
            s+=i.getVal()
        return s 

    def totalChargesV(self):
        s=0
        for i in self.chargesV:
            s+=i.getVal()
        return s

    def totalCharges(self):
        return(self.totalChargesF()+self.totalChargesV())
    
    def __str__(self):
        c="Charges fixe:\n"
        for i in self.chargesF:
            c+="\t"+str(i)+"\n"
        c+="Charges variables:\n"
        for i in self.chargesV:
            c+="\t"+str(i)+"\n"
        return c

#tst
"""
tst=Charges()
tst.addChargesF("ratio",1000)
tst.addChargesV("ratio2",200)
print(tst.toString())
print(tst.totalChargesF())
print(tst.totalChargesV())
print(tst.totalCharges())

"""

import Frequentation 
import Sport
import Five 
import Beach
import Padel
import config.config as cfg
import Revenue 
import Charges
import Semaine
import Abonnements as ab
import Date

@staticmethod
def buildFive(hc_rate, hp_rate, nb_anniversaires):
    freq = Frequentation.Frequentation(hc_rate, hp_rate, nb_anniversaires)
    five = Five.Five(freq)
    return five

@staticmethod
def buildBeach(hc_rate, hp_rate, nb_anniversaires):
    freq = Frequentation.Frequentation(hc_rate, hp_rate, nb_anniversaires)
    beach = Beach.Beach(freq)
    return beach

@staticmethod
def buildPadel(hc_rate, hp_rate, nb_anniversaires):
    freq = Frequentation.Frequentation(hc_rate, hp_rate, nb_anniversaires)
    padel = Padel.Padel(freq)
    return padel

@staticmethod
def buildRevenus():
    return Revenue.Revenus()

@staticmethod
def revAbos(nb_sub):
    return ab.revenuSubscribers(nb_sub)-ab.lossSubscribers(nb_sub)


def buildCharges():
    return Charges.Charges()
@staticmethod
def buildSemaine(nbSub,freq,revenus,charges,date):
    return Semaine.Semaine(nbSub,freq,revenus,charges,date)


   

beach=buildBeach(0.8,0.6,2)
five=buildFive(0.8,0.6,2)
padel=buildPadel(0.8,0.6,2)

rev=buildRevenus()
rev.addRevenu(Revenue.Revenu("Revenus abonements",revAbos(100)))
rev.addRevenu(Revenue.Revenu("Revenus Five",five.getRevenu()))
rev.addRevenu(Revenue.Revenu("Revenus Beach",beach.getRevenu()))
rev.addRevenu(Revenue.Revenu("Revenus Padel",padel.getRevenu()))

charge=buildCharges()
charge.addChargeF(Charges.Charge("Electricité",1000))
charge.addChargeF(Charges.Charge("Eau",2000))
charge.addChargeV(Charges.Charge("Croquette",3000))

date=Date.Date(1,1)
freq=Frequentation.Frequentation(0.8,0.6,2)
semaine=buildSemaine(100,freq,rev,charge,date)
semaines= Semaine.Semaines()
semaines.addSemaine(semaine)
print(semaines)

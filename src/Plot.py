import config.config as cfg
import charges as c 
import matplotlib.pyplot as plt
import main as m
#Affiche les revenus en fonction du taux d'abonnement
def plotSub(hp_Rate,hc_Rate):
    x = []
    y = []
    for i in range(0,100):
        x.append(i*0.01)
        y.append(Revenue(i*0.01,hp_Rate,hc_Rate))
    plt.plot(x,y)
    plt.show()

#Affiche les revenus en fonction du taux de rempliement  des hp et des hc 
#Affiche les revenus en fonction du nb moyen de vente au bar 
def plotBar(hp_Rate,hc_Rate,sub_rate):
    x = []
    y = []
    z=[]
    for i in range(2,10):
        x.append(i*0.1)
        y.append(m.RevenueBar(i*0.1,m.TotVisitors(cfg.HOURS,cfg.NB_BEACH,cfg.NB_FIVE,cfg.NB_PADEL),0.7))
        z.append(c.chargesV["bar"])
    plt.grid()
    plt.xlabel("Ticket Moyen")
    plt.ylabel("Revenus du bar en fonction du ticket moyen")
    plt.title("Revenus du bar en fonction du ticket moyen")
    plt.legend(["Revenus du bar","Charges du bar"])
    plt.plot(x,y)
    plt.plot(x,z)
    plt.show()
#Affiche les revenus en fonction du taux de rempliement  des hp et des hc
def plotRevenue(hp_Rate,hc_Rate,sub_rate):
    x = []
    y = []
    z=[]
    for i in range(0,100):
        x.append(i*0.01)
        y.append(m.Revenue(i*0.01,hp_Rate,hc_Rate)+m.RevenueBar(2,m.TotVisitors(cfg.HOURS,cfg.NB_BEACH,cfg.NB_FIVE,cfg.NB_PADEL),0.7))
        z.append(c.chargesV["bar"])
    plt.plot(x,y)
    plt.plot(x,z)
    plt.show()
plotRevenue(0.9,0.6,0.1)
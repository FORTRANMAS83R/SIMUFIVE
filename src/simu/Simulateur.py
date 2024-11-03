import sys
import os
import argparse
import matplotlib.pyplot as plt

# Ajouter le répertoire parent à sys.path
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
if parent_directory not in sys.path:
    sys.path.append(parent_directory)
import src.config.config as config
from src.simu.Sport import Sport
from src.simu.Bar import Bar
from src.simu.Semaine import Semaine
from src.simu.Semaine import Semaines
from openpyxl import Workbook


"""
Classe Simulateur, stocke des objets sports et leurs difffférentes copies au cours des semaines. 
Permetant ainsi de simuler l'évolution des sports au cours du temps.
"""
class Simulateur: 
    def __init__(self, config): 
        self.duree = config.duree_simu
        self.Five = Sport()
        self.Five.set_config(config.Five)
        self.Beach = Sport()
        self.Beach.set_config(config.Beach)
        self.Padel = Sport()
        self.Padel.set_config(config.Padel)
        self.Bar = Bar()
        self.Bar.set_config(config.Bar)
        self.semaines = []
        self.revenus = 0
    

    #Ajoute une semaine à la simulation

    def add(self, semaine):
        self.semaines.append(semaine)
        self.revenus += semaine.five.revenu + semaine.beach.revenu + semaine.padel.revenu + semaine.bar.revenus
    
    #Fait évoluer les sports de la simulation
    
    def evolve(self, i): 
        self.Five.evolve(i)
        self.Beach.evolve(i)
        self.Padel.evolve(i)
        self.Bar.evolve(i)
    
    def plot(self):
        n_semaine=[]
        res_five=[]
        res_beach=[]
        res_padel=[]
        CA=[]
        i=0
        for semaine in self.semaines:
            n_semaine.append(i)
            res_five.append(semaine.five.revenu)
            res_beach.append(semaine.beach.revenu)
            res_padel.append(semaine.padel.revenu)
            
            i+=1

        plt.plot(n_semaine,res_five,label="Five")
        plt.plot(n_semaine,res_beach,label="Beach")
        plt.plot(n_semaine,res_padel,label="Padel")
        plt.xlabel("Semaine")
        plt.ylabel("Revenu [€]")
        plt.legend()
        plt.show()

    #Lance la simulation
    def run(self): 
        for i in range(self.duree): 
            curr_semaine = Semaine()  
            self.evolve(i)  
            curr_semaine.add(self.Five.clone(), self.Beach.clone(), self.Padel.clone(), self.Bar.clone())
            print(str(self.Bar))
            self.add(curr_semaine)

    def toXlsx(self, fileName): 
        # Put simulation into an excel file
        # First sheet is for the global simulation (raw data)
        # Second sheet is for the mean CA per week, month, year
        wb = Workbook()

        # First sheet
        ws = wb.active
        ws.title = "Simulation"
        ws.append(["Semaine", "Five", "Beach", "Padel"])
        for i in range(len(self.semaines)):
            semaine = self.semaines[i]
            ws.append([i, semaine.five.revenu, semaine.beach.revenu, semaine.padel.revenu])
        
        # Write file
        wb.save(fileName + ".xlsx")



def start(config_path):
    cfg = config.init(config_path)
    simu = Simulateur(cfg)
    simu.run()
    print(simu.revenus)
    return simu



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script pour traiter un fichier.')
    parser.add_argument('file_name', type=str, help='Le nom du fichier à traiter')
    parser.add_argument('--xlsx', type=str, help='Le nom du fichier excel de sortie (sans extension)')
    args = parser.parse_args()
    
    simu = start(args.file_name)
    simu.plot()

    if(args.xlsx):
        simu.toXlsx(args.xlsx)
    print("Simulation done !")
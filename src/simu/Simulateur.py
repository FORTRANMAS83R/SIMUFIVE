import sys
import os
import argparse

# Ajouter le répertoire parent à sys.path
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
if parent_directory not in sys.path:
    sys.path.append(parent_directory)
import src.config.config as config
from src.simu.Sport import Sport
from src.simu.Semaine import Semaine
from src.simu.Semaine import Semaines
from openpyxl import Workbook

class Simulateur: 
    def __init__(self, config): 
        self.duree = config.duree_simu
        self.Five = Sport()
        self.Five.set_config(config.Five)
        self.Beach = Sport()
        self.Beach.set_config(config.Beach)
        self.Padel = Sport()
        self.Padel.set_config(config.Padel)
     #   self.Bar = Bar(config.Bar) PAS ENCORE IMPLEMENTE
        self.semaines = Semaines()

    def evolve(self, i): 
        self.Five.evolve(i)
        self.Beach.evolve(i)
        self.Padel.evolve(i)
       # self.Bar.evolve(i)

    def run(self): 
        for i in range(self.duree): 
            curr_semaine = Semaine()  
            self.evolve(i)  
            curr_semaine.add(self.Five.clone(), self.Beach.clone(), self.Padel.clone())
            self.semaines.add(curr_semaine)
    def plot(self): 
        self.semaines.plot()

    def toXlsx(self, fileName): 
        # Put simulation into an excel file
        # First sheet is for the global simulation (raw data)
        # Second sheet is for the mean CA per week, month, year
        wb = Workbook()

        # First sheet
        ws = wb.active
        ws.title = "Simulation"
        ws.append(["Semaine", "Five", "Beach", "Padel"])
        for i in range(len(self.semaines.semaines)):
            semaine = self.semaines.semaines[i]
            ws.append([i, semaine.five.revenu, semaine.beach.revenu, semaine.padel.revenu])
        
        # Write file
        wb.save(fileName + ".xlsx")



def start(config_path):
    cfg = config.init(config_path)
    simu = Simulateur(cfg)
    simu.run()
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
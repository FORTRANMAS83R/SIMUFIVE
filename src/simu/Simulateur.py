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



def start(config_path):
    cfg = config.init(config_path)
    simu = Simulateur(cfg)
    simu.run()
    return simu



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script pour traiter un fichier.')
    parser.add_argument('file_name', type=str, help='Le nom du fichier à traiter')
    args = parser.parse_args()
    
    simu = start(args.file_name)
    simu.plot()
    print("Simulation done !")
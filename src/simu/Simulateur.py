import sys
import os
import argparse
import matplotlib.pyplot as plt
import warnings
import time


# Ajouter le répertoire parent à sys.path
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
if parent_directory not in sys.path:
    sys.path.append(parent_directory)
import src.config.config as config
from src.simu.Sport import Sport
from src.simu.Bar import Bar
from src.simu.Semaine import Semaine
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
            self.add(curr_semaine)

    def toXlsx(self, fileName): 
        # Put simulation into an excel file
        # First sheet is for the global simulation (raw data)
        # Second sheet is for the mean CA per week, month, year
        wb = Workbook()

        # First sheet
        ws = wb.active
        ws.title = "Simulation"
        ws.append(["Semaine", "Revenus Five", "Revenus Beach", "Revenus Padel", "Revenus Bar", "Reservations Five HC", "Reservations Five HP", "Reservations Beach HC", "Reservations Beach HP", "Reservations Padel HC", "Reservations Padel HP", "Affluence Bar", "% Five", "% Beach", "% Padel", "% Bar"])
        for i in range(len(self.semaines)):
            semaine = self.semaines[i]
            ws.append([i, semaine.five.revenu, semaine.beach.revenu, semaine.padel.revenu, semaine.bar.revenus, semaine.five.freq.res_hc, semaine.five.freq.res_hp, semaine.beach.freq.res_hc, semaine.beach.freq.res_hp, semaine.padel.freq.res_hc, semaine.padel.freq.res_hp, semaine.bar.affluence, semaine.repartition["Five"], semaine.repartition["Beach"], semaine.repartition["Padel"], semaine.repartition["Bar"]])
        
        # Second sheet
        ws = wb.create_sheet(title="Moyennes")
        ws.append(["Période", "Revenus Five", "Revenus Beach", "Revenus Padel", "Revenus Bar"])
        ws.append(["Semaine", sum([semaine.five.revenu for semaine in self.semaines])/len(self.semaines), sum([semaine.beach.revenu for semaine in self.semaines])/len(self.semaines), sum([semaine.padel.revenu for semaine in self.semaines])/len(self.semaines), sum([semaine.bar.revenus for semaine in self.semaines])/len(self.semaines)])
        ws.append(["Mois", sum([semaine.five.revenu for semaine in self.semaines])/len(self.semaines)*4, sum([semaine.beach.revenu for semaine in self.semaines])/len(self.semaines)*4, sum([semaine.padel.revenu for semaine in self.semaines])/len(self.semaines)*4, sum([semaine.bar.revenus for semaine in self.semaines])/len(self.semaines)*4])
        ws.append(["Année", sum([semaine.five.revenu for semaine in self.semaines])/len(self.semaines)*52, sum([semaine.beach.revenu for semaine in self.semaines])/len(self.semaines)*52, sum([semaine.padel.revenu for semaine in self.semaines])/len(self.semaines)*52, sum([semaine.bar.revenus for semaine in self.semaines])/len(self.semaines)*52])

        # Third sheet
        ws = wb.create_sheet(title="Configurations")
        ws.append(["Sport", "Nombre terrain", "Prix HC", "Prix HP", "Freq Init HC", "Freq Max HC", "Freq Init HP", "Freq Max HP"])
        ws.append(["Five", self.Five.nb_terrains, self.Five.prix_hc, self.Five.prix_hp, self.Five.freq.freq_init_hc, self.Five.freq.freq_max_hc, self.Five.freq.freq_init_hp, self.Five.freq.freq_max_hp])
        ws.append(["Beach", self.Beach.nb_terrains, self.Beach.prix_hc, self.Beach.prix_hp, self.Beach.freq.freq_init_hc, self.Beach.freq.freq_max_hc, self.Beach.freq.freq_init_hp, self.Beach.freq.freq_max_hp])
        ws.append(["Padel", self.Padel.nb_terrains, self.Padel.prix_hc, self.Padel.prix_hp, self.Padel.freq.freq_init_hc, self.Padel.freq.freq_max_hc, self.Padel.freq.freq_init_hp, self.Padel.freq.freq_max_hp])

        # Write file
        wb.save(fileName + ".xlsx")


def start_multi_var(params_var: list, init_val: list, nb_simu: int, step: list, config_path: str) -> list:
    if not isinstance(params_var, list) or not isinstance(init_val, list) or not isinstance(step, list):
        raise ValueError("params_var, init_val and step doivent êter des listes ! start_multi_var(params_var: list, init_val: list, nb_simu: int, step: list, config_path: str) -> list")
    if len(params_var) != len(init_val) or len(params_var) != len(step):
        raise ValueError("params_var, init_val et step doivent avoir la même taille !")
    param_init = [config.stocker_param_init(config_path, param_var) for param_var in params_var]
    simulations = []
    for i in range(nb_simu):
        [config.modifier_parametre(config_path, params_var[j], init_val[j] + i*step[j]) for j in range(len(params_var))]
        simulations.append(start(config_path))
    return simulations

def start(config_path):
    cfg = config.init(config_path)
    simu = Simulateur(cfg)
    simu.run()
    return simu



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script pour traiter un fichier.')
    parser.add_argument('file_name', type=str, help='Le nom du fichier à traiter')
    parser.add_argument('--xlsx', type=str, help='Le nom du fichier excel de sortie (sans extension)')
    parser.add_argument('--param_var', nargs = '+', help='Lancer une simulation avec un ou plusieurs triplets de paramètres variables (nom_param, val_init, step)')
    parser.add_argument("--nb_simu", type=int, help="Le nombre de simulations à lancer (inutile si --param-var n'est utilisé)")
    parser.add_argument("-time", action="store_true", help="Afficher le temps d'exécution")
    args = parser.parse_args()
    print("Starting simulation...")
    if(args.time):
        start_time = time.time()
    if(args.param_var):
        if(len(args.param_var)%3 != 0):
            raise ValueError("Le nombre d'arguments pour --param_var doit être un multiple de 3 !(nom_param, val_init, step)")
        params_var = []
        val_init = []
        step = []
        for i in range(0, len(args.param_var), 3):
            params_var.append(args.param_var[i])    
            val_init.append(float(args.param_var[i+1]))
            step.append(float(args.param_var[i+2]))
        if(args.nb_simu):
            nb_simu = args.nb_simu
        else:
            nb_simu = 1
            warnings.warn("Le nombre de simulations n'a pas été spécifié, par défaut nb_simu = 1")
        
        simulations = start_multi_var(params_var, val_init, nb_simu, step, args.file_name)
    else: 
        if(args.nb_simu):
            warnings.warn("Attention : --nb_simu est ignoré car --param-var n’est pas actif")
        simu = start(args.file_name)
        simu.plot()
        if(args.xlsx):
            simu.toXlsx(args.xlsx)
    if(args.time):
        print("Execution time : %s seconds" % (round((time.time() - start_time),1)))
    print("Simulation done !")
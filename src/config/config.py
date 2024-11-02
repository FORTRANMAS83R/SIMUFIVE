
import json
class BarSpeConfig: 
    def __init__(self): 
        self.lambda_h_c = None
        self.lambda_h_p = None
        self.mu_h_c = None
        self.mu_h_p = None
        self.sigma_h_c = None
        self.sigma_h_p = None

    def set_Bar(self, config: dict):
        self.lambda_h_c = config["lambda_h_c"]
        self.lambda_h_p = config["lambda_h_p"]
        self.mu_h_c = config["mu_h_c"]
        self.mu_h_p = config["mu_h_p"]
        self.sigma_h_c = config["sigma_h_c"]
        self.sigma_h_p = config["sigma_h_p"]


class BarEvenementConfig(BarSpeConfig): 
    def __init__(self):
        super()
        self.frequence_occurence = None
        self.occurence_inter_semaine = None
        self.periode = None
    
    def set_Bar_evenement(self, config: dict): 
        super().set_Bar(config)
        self.frequence_occurence = config["frequence_occurence"]
        self.occurence_inter_semaine = config["occurence_inter_semaine"]
        self.periode = config["periode"]
class BarConfig:
    def __init__(self):
        self.semaine = BarSpeConfig()
        self.weekend = BarSpeConfig()
        self.evenements = BarEvenementConfig()
    def set_config(self, config):
        self.semaine.set_Bar(config['freq']['semaine'])
        self.weekend.set_Bar(config['freq']['week-end'])
        self.evenements.set_Bar_evenement(config['freq']['evenements'])


class SportConfig:
    def __init__(self): 
        self.freq = FrequentationConfig()
        self.nb_terrains = None
    def set_sport(self, freq, prix_hc, prix_hp, nb): 
        if isinstance(nb, int) == False: 
            raise ValueError("Le nombre de terrains doit être un entier")
        if nb < 1: 
            raise ValueError("Le nombre de terrains doit être supérieur ou égal à 1")
        self.freq.set_freq(freq)
        self.nb_terrains = nb
        self.prix_hc = prix_hc
        self.prix_hp = prix_hp
    def __str__(self):
        return "Fréquentation: " + str(self.freq) + "Nombre de terrains: " + str(self.nb_terrains) + "\n"

class FrequentationConfig: 
    def __init__(self): 
        self.freq_init_hc = None
        self.freq_max_hc = None
        self.var_hc = None
        self.type_evo_hc = None
        self.taux_evo_hc = None

        self.freq_init_hp = None
        self.freq_max_hp = None
        self.var_hp = None
        self.type_evo_hp = None
        self.taux_evo_hp = None

    def set_freq(self,config): 
        if not isinstance(config, dict): 
            raise ValueError("La configuration doit être un dictionnaire")
        self.freq_init_hc = config['freq_init_hc']
        self.freq_max_hc = config['freq_max_hc']
        self.var_hc = config['var_hc']
        self.type_evo_hc = config['type_evo_hc']
        self.taux_evo_hc = config['taux_evo_hc']

        self.freq_init_hp = config['freq_init_hp']
        self.freq_max_hp = config['freq_max_hp']
        self.var_hp = config['var_hp']
        self.type_evo_hp = config['type_evo_hp']
        self.taux_evo_hp = config['taux_evo_hp']
    def __str__(self):
        return "Fréquentation en heure creuse: \n" + "Fréquence initiale: " + str(self.freq_init_hc) + "\nFréquence maximale: " + str(self.freq_max_hc) + "\nVariance: " + str(self.var_hc) + "\nType d'évolution: " + str(self.type_evo_hc) + "\nTaux d'évolution: " + str(self.taux_evo_hc) + "\n" + "Fréquentation en heure pleine: \n" + "Fréquence initiale: " + str(self.freq_init_hp) + "\nFréquence maximale: " + str(self.freq_max_hp) + "\nVariance: " + str(self.var_hp) + "\nType d'évolution: " + str(self.type_evo_hp) + "\nTaux d'évolution: " + str(self.taux_evo_hp) + "\n"
    

        
class Config: 
    def __init__(self):
        self.duree_simu = None 
        self.Five = SportConfig()
        self.Beach = SportConfig()
        self.Padel = SportConfig()
        self.Bar = BarConfig()
    def set_five(self, freq, prix_hc, prix_hp, nb): 
        self.Five.set_sport(freq, prix_hc, prix_hp, nb)
    def set_beach(self, freq, prix_hc, prix_hp, nb):
        self.Beach.set_sport(freq, prix_hc, prix_hp, nb)
    def set_padel(self, freq, prix_hc, prix_hp, nb):
        self.Padel.set_sport(freq, prix_hc, prix_hp, nb)
    def set_Bar(self, config):
        self.Bar.set_config(config)
    def set_duree_simu(self, duree): 
        if not isinstance(duree, int): 
            raise ValueError("La durée de la simulation doit être un entier")
        self.duree_simu = duree
    def __str__(self): 
        return "Durée de la simulation: " + str(self.duree_simu) + "\n" + str(self.Five) + "\n" + str(self.Beach) + "\n" + str(self.Padel) + "\n"
    

def init(path): 
    config = Config()

    # Read the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Set the configuration values
    config.set_duree_simu(data['duree_simu'])

    # Set values for each sport
    config.set_five(data['Five']['freq'], data['Five']['prix_hc'], data['Five']['prix_hp'], data['Five']['nb_terrains'])
    config.set_beach(data['Beach']['freq'], data['Beach']['prix_hc'], data['Beach']['prix_hp'], data['Beach']['nb_terrains'])
    config.set_padel(data['Padel']['freq'], data['Padel']['prix_hc'], data['Padel']['prix_hp'], data['Padel']['nb_terrains'])
    config.set_Bar(data['Bar'])


    return config



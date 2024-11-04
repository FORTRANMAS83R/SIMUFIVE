import src.config.param as param
import numpy as np

@staticmethod
def modelisation(lbd, mu, sigma, nb_h):   
    revenus = 0
    affluence = 0
    tirage = np.random.poisson(lbd, nb_h)
    for i in range(len(tirage)):
        for j in range(tirage[i]):
            taille_groupe = np.random.uniform(2,5)
            el_rev = np.random.normal(mu,sigma) * taille_groupe 
            affluence += taille_groupe 
            revenus += el_rev    
    return revenus, affluence
class Bar: 
    def __init__(self): 
        self.affluence = 0
        self.revenus = 0
        self.config = None
    
    def set_config(self, config):
        self.config = config
    
    def clone(self):
        clone = Bar()
        clone.config = self.config
        clone.affluence = self.affluence
        clone.revenus = self.revenus
        return clone

    def evolve(self, i):
        nb_j_restant_semaine = 5
        nb_j_restant_weekend = 2
        self.revenus = 0 
        self.affluence = 0 
        if(i%self.config.evenements.frequence_occurence==0):
            for k in range(self.config.evenements.occurence_inter_semaine): 
                if(self.config.evenements.periode == 'semaine'): 
                    rev_jour, att_jour = self.jour(param.SEMAINE_NB_HC_JOUR, param.SEMAINE_NB_HP_JOUR, self.config.evenements.lambda_h_c, self.config.evenements.lambda_h_p, self.config.evenements.mu_h_c, self.config.evenements.mu_h_p, self.config.evenements.sigma_h_c, self.config.evenements.sigma_h_p)
                    nb_j_restant_semaine -= 1
                elif(self.config.evenements.periode == 'week-end'): 
                    rev_jour, att_jour = self.jour(param.WEEKEND_NB_HC_JOUR, param.WEEKEND_NB_HP_JOUR, self.config.evenements.lambda_h_c, self.config.evenements.lambda_h_p, self.config.evenements.mu_h_c, self.config.evenements.mu_h_p, self.config.evenements.sigma_h_c, self.config.evenements.sigma_h_p)
                    nb_j_restant_weekend -= 1
                else: 
                    raise ValueError("type de période inconnue ! Doit être doit 'semaine' soit 'week-end'")
                self.revenus += rev_jour
                self.affluence += att_jour
        for k in range(nb_j_restant_semaine): 
            rev_jour, att_jour = self.jour(param.SEMAINE_NB_HC_JOUR, param.SEMAINE_NB_HP_JOUR, self.config.semaine.lambda_h_c, self.config.semaine.lambda_h_p, self.config.semaine.mu_h_c, self.config.semaine.mu_h_p, self.config.semaine.sigma_h_c, self.config.semaine.sigma_h_p)
            self.revenus += rev_jour
            self.affluence += att_jour
        for k in range(nb_j_restant_weekend): 
            rev_jour, att_jour = self.jour(param.WEEKEND_NB_HC_JOUR, param.WEEKEND_NB_HP_JOUR, self.config.weekend.lambda_h_c, self.config.weekend.lambda_h_p, self.config.weekend.mu_h_c, self.config.weekend.mu_h_p, self.config.weekend.sigma_h_c, self.config.weekend.sigma_h_p)
            self.revenus += rev_jour
            self.affluence += att_jour
    
    def jour(self, nb_hc, nb_hp, lambda_hc, lambda_hp, mu_hc, mu_hp, sigma_hc, sigma_hp): 
        #Le nombre d'arrivée est dimensionné par heure, donc le nombre d'intervalles est égal au niombre d'heures
        revenus = 0
        affluence = 0
        #Pour les heures creuses 
        rev, aff = modelisation(lambda_hc, mu_hc, sigma_hc, nb_hc)
        revenus += rev
        affluence += aff

        #Pour les heures pleines
        rev, aff = modelisation(lambda_hp, mu_hp, sigma_hp, nb_hp)
        revenus += rev
        affluence += aff
        return revenus, affluence
    def __str__(self):
        return "Revenus: " + str(self.revenus) + "Affluence: " + str(self.affluence) + "\n"





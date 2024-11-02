import src.config.param as param
class Bar: 
    def __init__(self): 
        self.affluence = 0
        self.revenus = 0
        self.config = None
    
    def set_config(self, config):
        self.config = config

    def evolve(self, i):
        nb_j_restant_semaine = 5
        nb_j_restant_weekend = 2
        self.revenus = 0 
        self.affluence = 0 
        if(i%self.config.evenements.frequence_occurence==0):
            for k in range(self.config.evenements.occurence_inter_semaine): 
                rev_jour, att_jour = self.jour(self.config.evenements.lambda_h_c, self.config.evenements.lambda_h_p, self.config.evenements.mu_h_c, self.config.evenements.mu_h_p, self.config.evenements.sigma_h_c, self.config.evenements.sigma_h_p)
                self.revenus += rev_jour
                self.affluence += att_jour
            if(self.config.evenements.periode == 'semaine'): 
                nb_j_restant_semaine -= 1
            elif(self.config.evenements.periode == 'week-end'): 
                nb_j_restant_weekend -= 1
            else: 
                print(self.config.evenements.periode)
                raise ValueError("type de période inconnue ! Doit être doit 'semaine' soit 'week-end'")
        for k in range(nb_j_restant_semaine): 
            rev_jour, att_jour = self.jour(self.config.semaine.lambda_h_c, self.config.semaine.lambda_h_p, self.config.semaine.mu_h_c, self.config.semaine.mu_h_p, self.config.semaine.sigma_h_c, self.config.semaine.sigma_h_p)
            self.revenus += rev_jour
            self.affluence += att_jour
        for k in range(nb_j_restant_weekend): 
            rev_jour, att_jour = self.jour(self.config.weekend.lambda_h_c, self.config.weekend.lambda_h_p, self.config.weekend.mu_h_c, self.config.weekend.mu_h_p, self.config.weekend.sigma_h_c, self.config.weekend.sigma_h_p)
            self.revenus += rev_jour
            self.affluence += att_jour
        

            


        
    
    def jour(self,lambda_hc, lambda_hp, mu_hc, mu_hp, sigma_hc, sigma_hp): 

       # return revenus, affluence
       return 0, 0




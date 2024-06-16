import config.config as cfg 
def TotVisitors(HOURS,NB_BEACH,NB_FIVE,NB_PADEL):
    return(HOURS*(NB_BEACH*cfg.NB_PLAYER_BEACH+NB_FIVE*cfg.NB_PLAYER_FIVE+NB_PADEL*cfg.NB_PLAYER_PADEL))
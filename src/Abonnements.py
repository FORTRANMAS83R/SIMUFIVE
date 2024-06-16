import Verify as v
import config.config as cfg

import config.config as cfg
def revenuSubscribers(nb_sub):
    return (nb_sub*cfg.SUBSCRIPTION_PRICE)

def lossSubscribers(nb_sub):
    return (nb_sub*((cfg.MEAN_PRICE_BEACH/cfg.NB_BEACH)+(cfg.MEAN_PRICE_FIVE/cfg.NB_FIVE)+(cfg.MEAN_PRICE_PADEL/cfg.NB_PADEL)))
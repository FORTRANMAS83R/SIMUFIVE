"""
Les horaires d'ouverture: 
    -Lundi/vendredi: 11h/00h 
    -Samedi & Dimanche: 10h/23h
    => ouvert 91h/semaine 
Les heures creuses:
    -En semaine: 11h/17h
    => heures creuses = 30h 
    => heures pleines = 61h 
"""
#config
HOURS=91
HC=30
HP=60

#Five 
NB_FIVE=2 
NB_PLAYER_FIVE=10
HC_PRICE_FIVE=80
HP_PRICE_FIVE=90

MEAN_PRICE_FIVE=(HC_PRICE_FIVE+HP_PRICE_FIVE)/(2*NB_PLAYER_FIVE)

#Beach price
NB_BEACH=1
NB_PLAYER_BEACH=10
HC_PRICE_BEACH=70
HP_PRICE_BEACH=80
MEAN_PRICE_BEACH=(HC_PRICE_BEACH+HP_PRICE_BEACH)/(2*NB_PLAYER_BEACH)

#Padel price
NB_PADEL=2
NB_PLAYER_PADEL=4
HC_PRICE_PADEL=32
HP_PRICE_PADEL=40
MEAN_PRICE_PADEL=(HC_PRICE_PADEL+HP_PRICE_PADEL)/(2*NB_PLAYER_PADEL)

#Subscription price
SUBSCRIPTION_PRICE=19.99
NB_SUBSCRIBERS=100

#Anniv price 
PRICE_ANNIV=200



charges = {
    "Eau": "200000000000.0",
    "Electricite": "100.0",
    "Salaires": "3000.0",
    "Assurance": "200.0",
    "Securite": "150.0",
    "Communication": "0.05"  
}

configExit={}
chargesExit={}



#DELTA 
deltaActive=True
deltaCharges = 5 
deltaFreq = 3
deltaNbAnniv=5
deltaSub=5


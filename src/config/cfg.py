

config ={
    "duree_simu":"Annee",
    "Five":{
        "freq_init":60,
        "evolution":{
            "type":"lineaire",
            "taux_evolution":2
        },
        "nb_terrains":3,
        "anniv_active":False
    },
    "Beach":{
        "freq_init":60,
        "evolution":{
            "type":"lineaire",
            "taux_evolution":2
        },
        "nb_terrains":3,
        "anniv_active":False
    },
    "Padel":{
        "freq_init":60,
        "evolution":{
            "type":"lineaire",
            "taux_evolution":2
        },
        "nb_terrains":3,
        "anniv_active":False
    },
    "Bar":{
        "taux_freq":42,
        "ticket_moyen":3,
        "marge":70,
        "freq_add":70

    },
    "charges" : {
        "Eau": 350,
        "Electricite": 700,
        "Abonnements": 360.0,
        "Matériels": 300.0,
        "Salaires": 4710.0,
        "Assurance": 1666.0,
        "Securite": 150.0,
        "Interêts":4000 #emprunts de 2000000 à 4%


    }
}

amortissement = {
    "terrain_five": {
        "nb_annees": 10,
        "valeur": 2*35000,
        "val_amortissement": 2*35000/120
    },
    "Beach": {
        "nb_annees": 10,
        "valeur": 35000,
        "val_amortissement": 35000/120
    },
    "Padel": {
        "nb_annees": 10,
        "valeur": 2*35000,
        "val_amortissement": 2*35000/120
    },
    "batiment" : {
        "nb_annees": 20,
        "valeur": 2000000,
        "val_amortissement": 2000000/240
    },
    "amenagement": {
        "nb_annees": 10,
        "valeur": 200000,
        "val_amortissement": 200000/120
    },
    "bureautique": {
        "nb_annees": 5,
        "valeur": 10000,
        "val_amortissement": 10000/60
    }
}


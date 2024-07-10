

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
        "Eau": 2000,
        "Electricite": 100.0,
        "Nettoyage": 100.0,
        "Abonnements": 1000.0,
        "Matériels": 1000.0,
        "Salaires": 3000.0,
        "Assurance": 200.0,
        "Securite": 150.0  
    }
}

amortissement = {
    "terrain_five": {
        "nb_annees": 10,
        "valeur": 35000
    },
    "Beach": {
        "nb_annees": 10,
        "valeur": 35000
    },
    "Padel": {
        "nb_annees": 10,
        "valeur": 35000
    },
    "batiment" : {
        "nb_annees": 20,
        "valeur": 2000000
    },
    "amenagement": {
        "nb_annees": 10,
        "valeur": 200000
    },
    "bureautique": {
        "nb_annees": 5,
        "valeur": 10000
    }
}


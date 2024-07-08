import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))

parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)

import config.cfg as cfg#import src.config.cfg #import config.config as cfg
from simu.main import buildSimu
from simu.Excel import dictToDataFrame
charges = cfg.config["charges"].copy()
# Sidebar
st.sidebar.header("Sélection de la période")
period_simu = st.sidebar.selectbox("Choisissez une période", ["Trimestre", "Semestre", "Annee", "3 ans"])

# Onglet 1
tab1, tab2 = st.tabs(["Paramètres d'évolution", "Charges"])

with tab1:
    st.header("Paramètres d'évolution")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("Five")
        cfg.config["Five"]["freq_init"] = st.slider("Fréquentation initiale", 1, 100, 50)
        cfg.config["Five"]["evolution"]["type"] = st.selectbox("Type d'évolution", ["lineaire", "Pas dispo"])
        if cfg.config["Five"]["evolution"]["type"] == "lineaire":
            cfg.config["Five"]["evolution"]["taux_evolution"] = st.slider("taux d'évolution", 0.0, 10.0, 1.0)
        else:
            param1_1 = st.slider("Paramètre 1", 0.0, 10.0, 1.0)
            param1_2 = st.slider("Paramètre 2", 0.0, 10.0, 1.0)
        st.subheader("Options supplémentaires")
        cfg.config["Five"]["nb_terrains"] = st.number_input("Nombre de terrains Five", 1, 10, 1)
        cfg.config["Five"]["anniv_active"] = st.checkbox("Activer les anniversaires Five")

    with col2:
        st.subheader("Beach")
        cfg.config["Beach"]["freq_init"] = st.slider("Fréquentation initiale", 1, 100, 50, key='freq2')
        cfg.config["Beach"]["evolution"]["type"] = st.selectbox("Type d'évolution", ["lineaire", "Pas dispo"], key='evo2')
        if cfg.config["Beach"]["evolution"]["type"] == "lineaire":
            cfg.config["Beach"]["evolution"]["taux_evolution"] = st.slider("taux d'évolution", 0.0, 10.0, 1.0, key='param2')
        else:
            param2_1 = st.slider("Paramètre 1", 0.0, 10.0, 1.0, key='param2_1')
            param2_2 = st.slider("Paramètre 2", 0.0, 10.0, 1.0, key='param2_2')
        st.subheader("Options supplémentaires")
        cfg.config["Beach"]["nb_terrains"] = st.number_input("Nombre de terrains Beach", 1, 10, 1)
        cfg.config["Beach"]["anniv_active"] = st.checkbox("Activer les anniversaires beach")

    with col3:
        st.subheader("Padel")
        cfg.config["Padel"]["freq_init"] = st.slider("Fréquentation initiale", 1, 100, 50, key='freq3')
        cfg.config["Padel"]["evolution"]["type"] = st.selectbox("Type d'évolution", ["lineaire", "Pas dispo"], key='evo3')
        if cfg.config["Padel"]["evolution"]["type"] == "lineaire":
            cfg.config["Padel"]["evolution"]["taux_evolution"] = st.slider("taux d'évolution", 0.0, 10.0, 1.0, key='param3')
        else:
            param3_1 = st.slider("Paramètre 1", 0.0, 10.0, 1.0, key='param3_1')
            param3_2 = st.slider("Paramètre 2", 0.0, 10.0, 1.0, key='param3_2')
        st.subheader("Options supplémentaires")
        cfg.config["Padel"]["nb_terrains"] = st.number_input("Nombre de terrains Padel", 1, 10, 1)
        cfg.config["Padel"]["anniv_active"] = st.checkbox("Activer les anniversaires Padel")
    with col4:
        st.subheader("Bar")
        cfg.config["Bar"]["taux_freq"] = st.slider("Taux de fréquentation", 1, 100, 50)
        cfg.config["Bar"]["ticket_moyen"] = st.slider("Ticket moyen", 1, 15, 3)
        cfg.config["Bar"]["marge"] = st.slider("Marge", 1, 100, 70)
        cfg.config["Bar"]["freq_add"] = st.slider("Fréquentation additionnelle", 1, 100, 70)
   
with tab2:
    st.header("Charges")
    #charges = cfg.charges_.copy()
    for charge, valeur in charges.items():
        charges[charge] = st.number_input(charge, value=valeur)

    if st.button("Ajouter une charge"):
        new_charge = st.text_input("Nom de la nouvelle charge")
        new_value = st.number_input("Valeur de la nouvelle charge", 0, 1000, 0)

        if st.button("Valider") and new_charge and new_value:
            charges[new_charge] = new_value

checkbox_visu=st.sidebar.checkbox("Visualiser la simulation")
checkbox_comptable=st.sidebar.checkbox("Visualiser les comptes de résultats")
button_launch=st.sidebar.button("Lancer la simulation")


if(button_launch):
    a=buildSimu()
    print("ok")
    #f_id=open("simu.txt","x")
    #f_id.write(str(a))
    dictToDataFrame(a)


    if(checkbox_visu):
        visualiser_simu()
    if(checkbox_comptable):
        visualiser_comptes()


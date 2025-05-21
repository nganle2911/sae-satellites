# Auteur: LE Thi Kim Ngan
# Date: 07/04/2025
## OBJECTIF: Mettre toutes les catégories pour chaque satellite - Version 2

# ----------------------------------------------------------------------
## Etape 1: Création d'une fichier txt (en scrapping) contenant toutes les catégories avec les chiffres numérotées 1- 55 => A FAIT (creation_fichier_categories.py)
## Etape 2: Pour chaque satellite, scrapping ses catégories du site n2yo => puis comparer celles avec la liste créée ci-dessus => pour récupérer le numéro correspondant avec le nom de catégorie

# ----------------------------------------------------------------------
## 1 - Accéder au fichier "Position des satellites avec constellation_avec virgule.csv" et ajouter une colonne vide s'appelant "Categories"
import os 
import pandas as pd 

chemin = "/Users/nganle2911/Documents/2425_FRANCE/SCIENCES-DES-DONNEES/IUT-Perpignan-Carcassonne/BUT1_2425/Semestre_2/SAE/Project_statistique_astrophysique_2_06_DI_SCALA/travaux_rendus/categories"

# Lire le fichier
df = pd.read_csv("./Position des satellites avec constellation_avec virgule.csv", sep=";", encoding="latin1")
nb_lignes = len(df.axes[0])
nb_colonnes = len(df.axes[1])
# print([nb_lignes, nb_colonnes])

# Création d'une colonne vide "Categories"
liste_vide = []
for i in range(nb_lignes):
    liste_vide.append("")

# Cette liste de chaînes vides va être maintenant ajoutée comme colonne au dataframe df, avec pour nom de colonne "Categories"
df = df.assign(Categories = liste_vide)


# ----------------------------------------------------------------------
## 2 - Parcourir chaque ligne du fichier => récupérer le NORAD ID => Accéder au site n2yo de chaque satellite en utilisant NORAD id récupéré 
import requests 
from bs4 import BeautifulSoup 

cpt = 0
for numero, ligne in df.iterrows():
    
    # Récupérer NORAD ID
    noradID = ligne["NORAD_number"]
    print("noradID: ", noradID)

    # Accéder au site n2yo en utilisant noradID récupéré
    req_satellite = requests.get(f"https://www.n2yo.com/satellite/?s={noradID}")

    if req_satellite.status_code == 200:
        html = req_satellite.text
        print(html)
        print("Page chargée avec succès!")
    else:
        html = ""
        print("Erreur du téléchargement!")


    cpt += 1
    if cpt == 2:
        break
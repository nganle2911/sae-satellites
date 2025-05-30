## REDUIRE DES CHAMPS DE GROS FICHIER

import os
import pandas as pd

chemin = "/Users/nganle2911/Documents/2425_FRANCE/SCIENCES-DES-DONNEES/IUT-Perpignan-Carcassonne/BUT1_2425/Semestre_2/SAE/Project-statistique-astrophysique_R2-06"

os.chdir(chemin)

# Lire le fichier gros: satellites_13052025_avec_categorie.csv
df = pd.read_csv("./categories/satellites_13052025_avec_categorie.csv", sep=";", encoding="latin1")

# Transformer des données en prenant 3 champs: Name, constellation, catégorie
champs_choisis = ["Name", "NORAD_number", "Revolution_number"]
df = df[champs_choisis]

## POUR REVOLUTION_NUMBER - Enlever des lignes contenant la révolution_number = 0 ou vide
df_nettoye = df[(df['Revolution_number'].notna()) & (df['Revolution_number'] != 0)]

df_nettoye.to_csv("./sae-satellites-git/analyse-revolution/df.csv", sep=";", encoding="latin1", index=False)


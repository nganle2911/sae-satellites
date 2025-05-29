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

df.to_csv("./sae-satellites-git/analyse-revolution/df.csv", sep=";", encoding="latin1", index=False)


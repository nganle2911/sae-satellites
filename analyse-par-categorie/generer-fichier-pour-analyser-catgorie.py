## Générer un fichier contenant 4 colonnes: Name, Norad_ID, categorie, nom_categorie

import os
import pandas as pd
import numpy as np

chemin = "/Users/nganle2911/Documents/2425_FRANCE/SCIENCES-DES-DONNEES/IUT-Perpignan-Carcassonne/BUT1_2425/Semestre_2/SAE/Project-statistique-astrophysique_R2-06"
os.chdir(chemin)

# Lire le fichier gros: satellites_13052025_avec_categorie.csv
df = pd.read_csv("./categories/satellites_13052025_avec_categorie.csv", sep=";", encoding="latin1")

# Transformer des données en prenant 3 champs: Name, Norad_ID, categorie
champs_choisis = ["Name", "NORAD_number", "categorie"]
df = df[champs_choisis]

# Ajouter "Sans catégorie" pour des satellites sans catégorie
df['categorie'] = df['categorie'].replace(['=""', '', 'NaN', None], np.nan)
df['categorie'] = df['categorie'].fillna("Inconnu")

# Sauvegarder df en tant que fichier csv
df.to_csv("./analyse-par-categorie/df.csv", sep=";", encoding="latin1", index=False)

## Diviser des catégories pour des satellites contenant plusieurs catégories

# Pour des satellites ayant plusieurs catégories => Ecrire dans un autre fichier pour détacher des catégories
# df_tranche = df.head(8)
nouv_df = []

for numero, ligne in df.iterrows():
    # Pour créer de nouvelles lignes pour satellites ayant plusieurs catégories
    cat = ligne['categorie'].split(",")

    if len(cat) > 1:
        for val in cat:
            nouv_df.append([ligne['Name'], ligne['NORAD_number'], val.strip(' ="')])
    else:
        nouv_df.append([ligne['Name'], ligne['NORAD_number'], cat[0].strip('="')])

# Convertir liste en dataframe
df_cat = pd.DataFrame(nouv_df, columns=['Name', 'NORAD_number', 'categorie'])
nblignes = len(df_cat.axes[0])

df_cat.to_csv("./analyse-par-categorie/df_cat.csv", sep=";", encoding="latin1", index=False)


## Ajouter une colonne de nom de catégorie dans un fichier df_cat

# Création d'une liste de constellation
liste_const = []

with open("./categories/fichier_categories.txt", "r", encoding="utf-8") as fichier:
    lignes_const = fichier.readlines()

for i in range(len(lignes_const)):
    nom_const = lignes_const[i].split(",")[-1].split("]")[0].split("'")[1]
    liste_const.append(nom_const)

# Ajouter une colonne vide "nom_categorie"
# Créer d'abord des lignes vides
liste_vide = []
for i in range(nblignes):
    liste_vide.append('')

df_cat_plusgros = df_cat.assign(nom_categorie = liste_vide)

# Ajouter des valeurs pour le champ "nom_categorie"
for numero, ligne in df_cat_plusgros.iterrows():
    cat_sat = ligne['categorie']

    if cat_sat != "Inconnu":
        cat_sat = int(cat_sat)
        df_cat_plusgros.loc[numero, 'nom_categorie'] = liste_const[cat_sat-1]
    else:
        df_cat_plusgros.loc[numero, 'nom_categorie'] = "Inconnu"

# Sauvegarder dans un autre fichier avec des 3 champs
df_cat_plusgros.to_csv("./analyse-par-categorie/df_cat_plusgros.csv", sep=";", encoding="latin1", index=False)

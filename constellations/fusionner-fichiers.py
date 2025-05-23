## Fusionner tous les fichiers par 1 heure

import os
import pandas as pd

chemin = "/Users/nganle2911/Documents/2425_FRANCE/SCIENCES-DES-DONNEES/IUT-Perpignan-Carcassonne/BUT1_2425/Semestre_2/SAE/Project-statistique-astrophysique_R2-06/satellites-par-constellations/generer-fichiers-csv-et-cartes-du-ciel/45nord/"

# 1. Indiquer le chemin du dossier où sont les fichiers .csv
dossier = f"{chemin}/0h/fichiers"

# 2. Lister tous les fichiers CSV dans ce dossier
fichiers_csv = sorted([f for f in os.listdir(dossier) if f.endswith(".csv")])


# 3. Créer une liste pour stocker les DataFrames
liste_df = []

# 4. Charger chaque fichier et l'ajouter à la liste
for fichier in fichiers_csv:
    chemin_complet = os.path.join(dossier, fichier)
    df = pd.read_csv(chemin_complet, sep=";", encoding="latin1")
    champs_choisis = ["Name", "categorie", "Nom_constellation"]
    df = df[champs_choisis]

    df["categorie"] = df["categorie"].fillna("Inconnue").replace("", "Inconnue")
    heure = fichier.split('_')[-1].split('.csv')[0].split('h')[0]
    minute = fichier.split('_')[-1].split('.csv')[0].split('h')[-1].split("m")[0]
    seconde = fichier.split('_')[-1].split('.csv')[0].split('h')[-1].split("m")[-1].split("s")[0]
    df['index'] = int(heure)*3600 + int(minute)*60 + int(seconde)
    liste_df.append(df)


# 5. Fusionner tous les DataFrames en un seul
df_total = pd.concat(liste_df, ignore_index=True)

# 6. Sauvegarder le fichier fusionné
df_total.to_csv(os.path.join(dossier, f"{chemin}/0h/fichier_fusionne.csv"), sep=";", index=False, encoding="utf-8")

print("Fusion terminée !")

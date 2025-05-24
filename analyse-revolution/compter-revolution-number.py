## Compter le nombre de révolution d'un satellite

import os
import pandas as pd
from datetime import datetime, timedelta

os.chdir("/Users/nganle2911/Documents/2425_FRANCE/SCIENCES-DES-DONNEES/IUT-Perpignan-Carcassonne/BUT1_2425/Semestre_2/SAE/Project-statistique-astrophysique_R2-06/sae-satellites-git")

# Lire le fichier gros
df = pd.read_csv("./categorie/Satellites_13052025_categorielles.csv", sep=";", encoding="latin1")

champs = ["Name", "LAUNCH_DATE", "Period(minutes)", "Epoch", "Revolution_number"]
df = df[champs]
df = df.loc[0,]
print(df)

# Lancement
date_lancement = datetime.strptime(df['LAUNCH_DATE'], "%d/%m/%Y")

# Epoch : jour 132.99185303 de 2025
# Jour 132 → 11 mai
epoch_jour = df['Epoch']
annee_epoch = "20" + str(int(epoch_jour))[:2]

# Convertir en date
epoch_base = datetime(2025, 1, 1)
delta_epoch = timedelta(days=epoch_jour)
date_epoch = epoch_base + delta_epoch
temps_epoch_minutes = delta_epoch.total_seconds() / 60

# Temps total en minutes
delta_temps = date_epoch - date_lancement
temps_total_minutes = delta_temps.total_seconds() / 60

# Période orbitale
periode = 132.60622784707064  # en minutes

# Nombre de révolutions depuis l'epoch
nb_revolution_epoch = temps_epoch_minutes / periode
print("\n")
print(f"Nombre de révolutions depuis l'epoch: {nb_revolution_epoch:.2f}")

# Nombre de révolutions
nb_revolutions = temps_total_minutes / periode

print("\n")
print(f"Nombre de révolutions estimé: {nb_revolutions:.2f}")

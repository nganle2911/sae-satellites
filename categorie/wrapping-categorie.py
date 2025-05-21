import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import html

# Télécharger jusqu'à "globalstar"

chemin_acces = "/Users/nganle2911/Documents/2425_FRANCE/SCIENCES-DES-DONNEES/IUT-Perpignan-Carcassonne/BUT1_2425/Semestre_2/SAE/Project-statistique-astrophysique_R2-06/categories"
os.chdir(chemin_acces)

sat_id = 36
req = requests.get(f"https://www.n2yo.com/satellites/?c={sat_id}&p=A")

dossierNORADid = "NORAD_ID_par_categorie"

# os.path.exist() - pour vérifier le chemin existe ou vérifier si le chemin vers le dossier TLE_telecharge existe
verifie_dossier = os.path.exists(f"{chemin_acces}/{dossierNORADid}")

# S'il n'existe pas, créer alors un nouveau dossier TLE_telecharge
if verifie_dossier != True:
    os.mkdir(dossierNORADid)


if req.status_code == 200:
    html_contenu = req.text
    # print(html)
    print("Page chargée avec succès!\n")
else:
    html_contenu = ""
    print("Erreur du téléchargement!")

# Récupérer le contenu par BeautifulSoup
soup = BeautifulSoup(html_contenu, "html.parser")

job_elements_tr = soup.find_all("tr")

job_element_title = soup.find_all("title")
title = job_element_title[0].decode_contents()
title_nettoye = html.unescape(title)

liste_id = []
for element in job_elements_tr[3:-2]:
    job_element_td = element.find_all("td")
    noradID = job_element_td[1].decode_contents()
    liste_id.append(noradID)

data = {}
data["NORAD_ID"] = liste_id

df = pd.DataFrame(data)

print("Lancement de la sauvegarde en CSV. Attendez...")
df.to_csv(f"./{dossierNORADid}/{title_nettoye}.csv", sep = ";", index = False, encoding = "latin1")
print("Fin du programme")
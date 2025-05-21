# Auteur: LE Thi Kim Ngan
# Date: 03/04/2025
## OBJECTIF: Création d'un fichier contenant une liste de catégories - Version 2

# ----------------------------------------------------------------------
## Etape 1: Création d'une fichier txt (en scrapping) contenant toutes les catégories avec les chiffres numérotées 1- 55
# Scrapping toutes les catégories
import requests
from bs4 import BeautifulSoup
import os
import html

# chemin_acces = "U:/BUT_1/semestre_2/SAE/6_Satellites/Travaux_a_rendre/categories"
chemin_acces = "/Users/nganle2911/Documents/2425_FRANCE/SCIENCES-DES-DONNEES/IUT-Perpignan-Carcassonne/BUT1_2425/Semestre_2/SAE/Project-statistique-astrophysique_R2-06/categories"
os.chdir(chemin_acces)

fichierCat = "fichier_categories.txt"

req_categories = requests.get("https://www.n2yo.com/satellites/")

if req_categories.status_code == 200:
    html_contenu = req_categories.text
    print("Page chargée avec succès!\n")
else:
    html_contenu = ""
    print("Erreur du téléchargement!")

# Récupérer le contenu par BeautifulSoup
soup = BeautifulSoup(html_contenu, "html.parser")

table_cat = soup.find(id="categoriestab")
elements_a = table_cat.findAll("a")

# Créer une liste de catégories après scapping
liste_cat = []
cpt = 0

for cat in elements_a:
    # print(cat)
    cpt += 1
    nom_cat = cat.decode_contents()
    nom_cat_nettoye = html.unescape(nom_cat)
    # print(cpt)
    # print(nom_cat)

    liste_cat.append([cpt, nom_cat_nettoye])

# print(liste_cat)

# # Vérifier le chemin existe ou vérifier si le chemin vers le fichier fichier_categories.txt existe
# verifie_fichier = os.path.exists(f"{chemin_acces}/{fichierCat}")
#
# # S'il n'existe pas, créer alors un nouveau fichier
# if verifie_fichier != True:
#     touch fichierCat

# Enregistrer cette liste_cat dans un fichier txt
with open(f'./{fichierCat}', 'w', encoding="utf-8") as f:
    for line in liste_cat:
        f.write(f"{line}\n")


# Stocker les dans un fichier avec des numéros


# ----------------------------------------------------------------------
## Etape 2: Pour chaque satellite, scrapping ses catégories du site n2yo => puis comparer celles avec la liste créée ci-dessus => pour récupérer le numéro correspondant avec le nom de catégorie







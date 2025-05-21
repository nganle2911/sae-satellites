## AJOUTER UNE COLONNE "CATEGORIE" POUR LE FICHIER SATELLITE FINAL

import os
os.chdir("/Users/nganle2911/Documents/2425_FRANCE/SCIENCES-DES-DONNEES/IUT-Perpignan-Carcassonne/BUT1_2425/Semestre_2/SAE/Project-statistique-astrophysique_R2-06/categories")

# Dossier contenant les fichiers scrappé
dossier_parent = "NORAD_ID_par_categorie"

# Le noms des fichiers seront lus automatiquement depuis le dossier
# dont le chemin est dans "dossier_parent"
# Ces fichiers sont des fichiers scrappés avec une colonne de n° NORAD obligatoire

contenu_du_dossier = os.listdir(dossier_parent)
listefichiers = sorted([fichier for fichier in contenu_du_dossier])
listefichiers = listefichiers[1:]


# Le n° de catégorie est forcément automatique : le n° de position du fichier dans "listefichiers"
liste_numeroscat_associes = list(range(1,len(listefichiers)+1))

# Pour information, affichage des n° de catégorie
print("Liste des n° de catégories construites :")
numero = 1
for fichier in listefichiers:
    print(numero,":",fichier)
    numero = numero + 1

# Nom de la colonne contenant le n° NORAD dans chaque fichier
nomdecolonne = 'NORAD_ID'

######################

import pandas as pd

# En cas d'encodage du fichier texte en "ANSI", c'est à dire en latin1, on informe pandas qu'on utilise l'encodage des caractères en "latin1" pour lire le contenu

# En cas d'encodage du fichier texte en "UTF-8", on informe pandas qu'on utilise l'encodage des caractères en utf-8 pour lire le contenu
df = pd.read_csv("Fichier satellite final nettoye_complet.csv",sep=";",encoding="latin1")


nblignes = len(df.axes[0])
print("\nNombre de satellites :",nblignes)

# Pour créer une nouvelle liste de chaînes de caractères vides qui contient autant de chaînes que de lignes du dataframe
liste_vide = []
for i in range(nblignes):
    liste_vide.append('')

df = df.assign(categorie = liste_vide)

######################
liste_de_dataframes =[]

for nomfichier in listefichiers:
    # "latin1" ou "utf-8" selon encodage, à choisir
    df_charge = pd.read_csv(dossier_parent+"/"+nomfichier,sep=";",encoding="utf-8")
    liste_de_dataframes.append(df_charge)

# Boucle sur les 20 premiers, adapter pour faire TOUT le fichier
cpt = 0
for numero,ligne in df.iterrows():
    noradid = ligne["NORAD_number"]
    # print("NORAD_number :",noradid)
    parcours = 0
    listecategories = []
    for df_test in liste_de_dataframes:
        if noradid in df_test[nomdecolonne].values:
            numero_de_categorie = liste_numeroscat_associes[parcours]
            listecategories.append(numero_de_categorie)
        parcours = parcours + 1

    # On trie dans l'ordre croissant des n° de catégories
    listecategories.sort()

    # On transforme le contenu dans "listecategories" en chaîne de caractère
    listecategories = [str(element) for element in listecategories]

    chaine_liste_categories = ",".join(listecategories)

    df.loc[numero,"categorie"] = chaine_liste_categories

    # Remplacer [1,1] = [1, 10]
    cat = ligne['categorie'].split(",")
    if cat == ["1","1"]:
        cat = ["1", "10"]


df.to_csv("Satellite_avec_colonne_categorielle_liste.csv",sep=";",index=False, encoding="latin1")
from random import *
from Exerciseur import *

ref="EqProduitIR" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

comp="Raisonner" # La compétence de l'exercice

consigne="Résoudre les equations produits suivantes" #La consigne générale

path="Ex_Raisonner/Exo_EquaProdIR.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    if index <4 :
        exo[index]=str(randint(1,9)**2)+"x^2"+ "-" + str(randint(1,9)**2) +"=0"
    # elif index <8 :
    #     str(randint(1,9)**2)+"x^2"+ "=" + str(randint(1,9)**2)
    else :
        exo[index]=facteur() + "^2=" + facteur() +"^2"


exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
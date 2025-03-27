from random import *
from Exerciseur import *

ref="EqProduitFacto" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

comp="Raisonner" # La compétence de l'exercice

consigne="Résoudre les equations produits suivantes" #La consigne générale

path="Ex_Raisonner/Exo_EquaProdFacto.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    FacteurA=facteur()
    if index <4 :
        exo[index]=FacteurA + facteur() + "+" + FacteurA + facteur() +"=0"
    elif index <8 :
        exo[index]=FacteurA + facteur() + "-" + FacteurA + facteur() +"=0"
    else :
        exo[index]=FacteurA + facteur() + "=" + plusmoinsdebut() + FacteurA + facteur()


exercices_auto(ref,nb,path,exo,comp,consigne,2) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
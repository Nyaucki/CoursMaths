from random import *
from Exerciseur import *

ref="EqProduit" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

comp="Calculer" # La compétence de l'exercice

consigne="Résoudre les equations produits suivantes" #La consigne générale

path="Ex_Calculer/Exo_EquaProduit.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    exo[index]="(" +plusmoinsdebut() + str(randint(1,10)) +"x" + plusmoins() + str(randint(1,10))+")("+plusmoinsdebut() +str(randint(1,10)) +"x" + plusmoins() + str(randint(1,10))+")=0"

exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
from random import *
from Exerciseur import *

ref="Test" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=20 # Le nombre d'exercice

comp="Calculer" # La compétence de l'exercice

consigne="Effectuer les calculs suivants" #La consigne générale

path="Test.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    exo[index]=plusmoins() + str(randint(1,20))
    for j in range (index//5 +1):
        exo[index]= exo[index] + plusmoins() + "("+plusmoins() + str(randint(1,20))+")"

exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
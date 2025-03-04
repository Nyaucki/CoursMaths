from random import *
from Exerciseur import *

ref="Test" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=20 # Le nombre d'exercice

path="Test.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    exo[index]=plusmoins() + str(randint(1,20))
    for j in range (index//5 +1):
        exo[index]= exo[index] + plusmoins() + "("+plusmoins() + str(randint(1,20))+")"

exercices_auto(ref,nb,path,exo) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 5eme argumant pour modifier ceci.

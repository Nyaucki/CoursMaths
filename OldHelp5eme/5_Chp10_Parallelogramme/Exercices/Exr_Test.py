from random import *
from Exerciseur import *

ref="Test" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

comp="Représenter" # La compétence de l'exercice

consigne="Tracer les parallélogrammes $ABCD$ suivants" #La consigne générale

path="Ex_Representer/Exo_Tracer.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    
    exo[index]="un rectangle tel que AB="+str(randint(1,5)) +"et BC="+str(randint(1,5))

exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
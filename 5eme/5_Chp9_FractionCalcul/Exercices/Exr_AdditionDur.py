from random import *
from Exerciseur import *

ref="AddDur" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=6 # Le nombre d'exercice

comp="" # La compétence de l'exercice

consigne="(Calculer) Effectuer les calculs suivants" #La consigne générale

path="Ex_Calculer/Exo_AdditionsDur.tex.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    exo[index]="\\dfrac{" + str(randint(1,20)) + "}{"+ str(randint(2,3)*randint(1,5)) + "}+\\dfrac{" + str(randint(1,20)) +"}{" + str(randint(7,9)*randint(1,2))+"}"

exercices_auto(ref,nb,path,exo,comp,consigne,6) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
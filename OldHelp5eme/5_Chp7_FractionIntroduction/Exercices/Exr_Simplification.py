from random import *
from Exerciseur import *

ref="Simplifier" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

path="Ex_Representer/Exo_Simplification.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

comp="Représntr"

consigne="Simplifier les fractions suivantes"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    rank=10
    if index >5:
        rank=20
    a,b,c=randint(2,rank),randint(2,rank),randint(2,rank//2)
    exo[index]="\\dfrac{"+str(a*c)+"}{"+str(b*c)+ "}=\\filling" 
    

exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.

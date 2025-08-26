from random import *
from Exerciseur import *

ref="PdtCroix" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

path="Ex_Calculer/Exo_PdtCroix.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

comp="Calculer"

consigne="Compléter avec = ou $\\neq $"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    rank=10
    if index >5:
        rank=25
    a,b,c,d=randint(2,rank),randint(2,rank),randint(2,rank),randint(0,1)
    exo[index]="\\dfrac{"+str(a)+"}{"+str(b)+ "}\\filling \\dfrac{ " + str(c*b)+"}{"+str(c*a+d)+"}"
    

exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.

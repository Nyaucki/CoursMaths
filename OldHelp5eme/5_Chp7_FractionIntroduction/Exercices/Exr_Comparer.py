from random import *
from Exerciseur import *

ref="Comparer" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

path="Ex_Calculer/Exo_Comparer.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

comp="Calculer"

consigne="Compléter avec > ou <"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    rank=10
    if index >5:
        rank=25
    a,b,c,d=1,1,1,1
    while a/b==c/d:
        a,b,c,d=randint(2,rank),randint(2,rank),randint(2,rank),randint(2,rank)
    exo[index]="\\dfrac{"+str(a)+"}{"+str(b)+ "}\\filling \\dfrac{ " + str(c)+"}{"+str(d)+"}"
    

exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.

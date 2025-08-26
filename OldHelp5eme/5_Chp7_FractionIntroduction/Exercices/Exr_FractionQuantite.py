from random import *
from Exerciseur import *

ref="FractionQuantite" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

path="Ex_Calculer/Exo_FractionQuantite.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

comp="Calculer"

consigne="Calculer"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    rank=10
    a,b=1,1
    if index >5:
        rank=20
    while a==b:
        a,b,c=randint(1,rank),randint(2,rank),randint(2,rank)
    if index<8:
        c=b*randint(2,rank)
    exo[index]="\\dfrac{"+str(a)+"}{"+str(b)+ "}\\text{~~de~~}"+str(c)+"=\\filling"
    

exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.

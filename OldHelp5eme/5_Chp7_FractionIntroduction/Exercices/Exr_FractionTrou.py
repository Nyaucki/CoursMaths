from random import *
from Exerciseur import *

ref="FractionTrou" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

path="Ex_Chercher/Exo_FractionsTrous.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

comp="Chercher"

consigne="Compléter pour rendre les fractions égales"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    rank=10
    if index >5:
        rank=25
    a,b,c=randint(2,rank),randint(2,rank),randint(2,rank)

    if index %4==0:
        exo[index]=" \\dfrac{"+str(a*c)+"}{\\text{\\filling[1cm]}}=\\dfrac{"+str(a)+"}{"+str(b)+ "}"
    if index %4==1:
        exo[index]="\\dfrac{"+str(a)+"}{"+str(b)+ "}= \\dfrac{\\text{\\filling[1cm]}}{"+str(b*c)+"}"
    if index %4==2:
        exo[index]="\\dfrac{"+str(a)+"}{"+str(b)+ "}= \\dfrac{"+str(a*c)+"}{\\text{\\filling[1cm]}}"
    if index %4==3:
        exo[index]=" \\dfrac{\\text{\\filling[1cm]}}{"+str(b*c)+"}=\\dfrac{"+str(a)+"}{"+str(b)+ "}"
    

exercices_auto(ref,nb,path,exo,comp,consigne) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.

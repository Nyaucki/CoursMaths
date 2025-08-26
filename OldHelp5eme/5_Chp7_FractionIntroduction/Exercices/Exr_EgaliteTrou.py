from random import *
from Exerciseur import *

ref="EgaliteTrou" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=20 # Le nombre d'exercice

path="Ex_Calculer/Exo_EgaliteTrou.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

consigne="Compléter pour rendre l'égalité vraie"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    a,b,c=randint(2,9),randint(2,9),1
    while b==a:
        b=randint(2,9)
    if index>6:
        c=randint(2,9)
    if index %3==0:
        exo[index]=str(a*c)+"\\times \\filling = "+str(b*c)
    if index %3==1:
        exo[index]=str(a*c)+"\\times \\dfrac{"+str(b)+"}{"+str(a)+ "}= \\filling"
    if index %3==2:
        exo[index]="\\filling \\times \\dfrac{"+str(b)+"}{"+str(a)+ "}= " + str(b*c)
    

exercices_auto(ref,nb,path,exo,"Calculer") # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.

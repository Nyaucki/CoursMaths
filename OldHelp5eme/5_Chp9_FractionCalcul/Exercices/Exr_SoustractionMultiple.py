from random import *
from Exerciseur import *

ref="SousMul" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=5 # Le nombre d'exercice

comp="" # La compétence de l'exercice

consigne="(Raisonner) Effectuer les calculs suivants" #La consigne générale

path="Ex_Raisonner/Exo_SousMultiple.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    if index<4 :
        den = randint(2,9)
        fact=randint(2,10)
        exo[index]="\\dfrac{" + str(randint(1,20)) + "}{"+ str(den) + "}-\\dfrac{" + str(randint(1,20)) +"}{" + str(den*fact)+"}"+plusmoins()+"\\dfrac{" + str(randint(1,20)) +"}{" + str(den*fact)+"}"
    else :
        den = randint(2,9)
        fact=randint(2,5)
        facto=fact+randint(4,7)
        exo[index]="\\dfrac{" + str(randint(1,20)) + "}{"+ str(den) + "}-\\dfrac{" + str(randint(1,20)) +"}{" + str(den*fact)+"}"+plusmoins()+"\\dfrac{" + str(randint(1,20)) +"}{" + str(den*facto)+"}"

exercices_auto(ref,nb,path,exo,comp,consigne,5) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
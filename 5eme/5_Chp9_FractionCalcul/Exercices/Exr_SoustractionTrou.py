from random import *
from Exerciseur import *

ref="SousTrou" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=10 # Le nombre d'exercice

comp="" # La compétence de l'exercice

consigne="(Chercher) Compléter pour rendre l'égalité vraie" #La consigne générale

path="Ex_Chercher/Exo_SoustractionsTrou.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    if index <4:
        den=randint(3,10)
        fact=randint(3,10)
        num1=randint(3,10)
        num2=randint(3,10)
        exo[index]="\\dfrac{\\dots}{"+ str( den ) + "}-\\dfrac{ "+str(num2)+"}{" + str(fact*den)+"}=\\dfrac{"+str(num1*fact - num2)+"}{"+str(fact*den)+"}"
    elif index<8 :
        den=randint(3,10)
        fact=randint(3,10)
        num1=randint(3,10)
        num2=randint(3,10)
        exo[index]="\\dfrac{" + str(num1) + "}{\\dots}-\\dfrac{ "+str(num2)+"}{" + str(fact*den)+"}=\\dfrac{"+str(num1*fact - num2)+"}{"+str(fact*den)+"}"
    else :
        den=randint(3,10)
        fact=randint(3,10)
        num1=randint(3,10)
        num2=randint(3,10)
        exo[index]="\\dfrac{" + str(num1) + "}{"+ str( den ) + "}-\\dfrac{ \\dots}{" + str(fact*den)+"}=\\dfrac{"+str(num1*fact - num2)+"}{"+str(fact*den)+"}"

exercices_auto(ref,nb,path,exo,comp,consigne,5) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
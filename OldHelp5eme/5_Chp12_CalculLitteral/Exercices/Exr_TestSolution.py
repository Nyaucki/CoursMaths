from random import *
from Exerciseur import *

ref="Tester" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=9 # Le nombre d'exercice

comp="Calculer" # La compétence de l'exercice

consigne="Le nombre donné est il solution de l'équation" #La consigne générale

path="Ex_Calculer/Exo_TestSolution.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

alphabet="azertyuiopqsdfghjklmwxcvbn"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    lettre=alphabet[randint(0,len(alphabet)-1)]
    a=randint(1,3)
    b=randint(2,10)
    c=randint(2,10)
    d=randint(1,2)
    if index<3:
        exo[index]="$$"+str(a)+"+"+str(6*b)+lettre+"="+str(6*c)+"$$ a t'il pour solution $"+lettre+"="+str((c-b)*6//a+randint(0,1))+"$"
    else:
        exo[index]="$$"+str(a)+"+"+str(2*b)+lettre+"="+str(d+a)+"+"+str(2*c)+lettre+"$$ a t'il pour solution $"+lettre+"="+str((c-b)*2//d+randint(0,1))+"$"
    

exercices_auto(ref,nb,path,exo,comp,consigne,3,False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
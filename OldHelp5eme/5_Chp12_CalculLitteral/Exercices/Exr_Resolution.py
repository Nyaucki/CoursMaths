from random import *
from Exerciseur import *

ref="Résoudre" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=18 # Le nombre d'exercice

comp="Calculer" # La compétence de l'exercice

consigne="Résoudre les équations suivantes" #La consigne générale

path="Ex_Calculer/Exo_ResoudreEquation.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

alphabet="azertyuiopqsdfghjklmwxcvbn"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    lettre=alphabet[randint(0,len(alphabet)-1)]
    a=randint(1,3)
    b=randint(2,10)
    c=randint(2,10)
    d=randint(1,2)
    if index<3:
        exo[index]=str(b)+lettre+"="+str(b*c)
    elif index<6:
        exo[index]=str(b)+lettre+"="+str(c)
    elif index<9:
        exo[index]=lettre+plusmoins()+str(b)+"="+str(c*(-1)**d)
    elif index<12 :
        exo[index]=str(a)+lettre+plusmoins()+str(b)+"="+str(c*(-1)**d)
    else :
        exo[index]=str(a)+lettre+plusmoins()+str(b)+"="+str(c*(-1)**d)+plusmoins()+str(a+d)+lettre
        

exercices_auto(ref,nb,path,exo,comp,consigne,3) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
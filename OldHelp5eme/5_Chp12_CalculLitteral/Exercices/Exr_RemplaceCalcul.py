from random import *
from Exerciseur import *

ref="Remplace" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=9 # Le nombre d'exercice

comp="Calculer" # La compétence de l'exercice

consigne="Effectuer les calculs suivants" #La consigne générale

path="Ex_Calculer/Exo_RemplaceCalcul.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

alphabet="azertyuiopqsdfghjklmwxcvbn"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    lettre=alphabet[randint(0,len(alphabet)-1)]
    exo[index]="$"+str(randint(2,10))+lettre+plusmoins()+str(randint(2,10))+plusmoins()+str(randint(2,10))+lettre+plusmoins()+str(randint(2,10))+"$ pour $"+lettre +"="+str(randint(-10,10))+"$"
    

exercices_auto(ref,nb,path,exo,comp,consigne,3,dollar=False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
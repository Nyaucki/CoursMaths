from random import *
from Exerciseur import *

ref="SimplifierEcriture" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=6 # Le nombre d'exercice

comp="Représenter" # La compétence de l'exercice

consigne="Simplifie l'écriture des expressions suivantes." #La consigne générale

path="Ex_Representer/Exo_SimplifieCalcul.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

alphabet="azertyuiopqsdfghjklmwxcvbn"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    lettre=alphabet[randint(0,len(alphabet)-1)]
    exo[index]=str(randint(1,4))+"\\times "+lettre+plusmoins()+str(randint(2,10))+plusmoins()+str(randint(2,10))+"\\times("+str(randint(-3,3))+"\\times "+lettre+plusmoins()+str(randint(2,10))+")"
    

exercices_auto(ref,nb,path,exo,comp,consigne,3) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
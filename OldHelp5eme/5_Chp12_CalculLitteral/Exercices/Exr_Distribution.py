from random import *
from Exerciseur import *

ref="Distributivite" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=9 # Le nombre d'exercice

comp="Calculer" # La compétence de l'exercice

consigne="Dévellope et réduit les expressions suivantes" #La consigne générale

path="Ex_Calculer/Exo_Distributivite.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

alphabet="azertyuiopqsdfghjklmwxcvbn"

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    lettre=alphabet[randint(0,len(alphabet)-1)]
    if index<3:
        exo[index]=str(randint(2,10))+"("+str(randint(1,2))+lettre+plusmoins()+str(randint(2,10))+")"
    elif index<6:
        exo[index]=str(randint(2,10))+lettre+"("+str(randint(1,2))+lettre+plusmoins()+str(randint(2,10))+")"
    else:
        exo[index]=str(randint(2,10))+lettre+"("+str(randint(1,2))+lettre+plusmoins()+str(randint(2,10))+")"+"+"+str(randint(2,10))+lettre+"("+str(randint(1,2))+lettre+plusmoins()+str(randint(2,10))+")"
    

exercices_auto(ref,nb,path,exo,comp,consigne,3) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
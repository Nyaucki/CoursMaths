from random import *
from Exerciseur import *

ref="CalcImage" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

comp="" # La compétence de l'exercice

consigne="(Calculer) Pour cette exercice, on considère les fonctions $f:x\\mapsto 2x+4$, $g:x\\mapsto x^2-9$ et $h:x\\mapsto (x+3)(-x+2)$" #La consigne générale

path="Ex_Calculer/Exo_DonnerImage.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

list_fonction=["$f","$g","$h"]

list_alea=[]
for index in range(nb):
    f,i =randint(0,2),randint(-15,15)
    while [f,i] in list_alea:
        f,i =randint(0,2),randint(-15,15)
    list_alea.append([f,i])

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    if index < nb/2:
        exo[index]=list_fonction[list_alea[index][0]]+"("+str(list_alea[index][1])+")=\\fillin[1cm]$"
    else : 
        exo[index]="L'image de "+str(list_alea[index][1])+ " par la fonction "+list_fonction[list_alea[index][0]]+"$ est \\fillin[1cm]"
        if index>nb-4:
            exo[index]+="\\columnbreak"

echangeur=[0,3,6,9,1,4,7,10,2,5,8,11]
exo_ordonne=list(range(nb))

for index in range(nb):
    exo_ordonne[echangeur[index]]=exo[index]


exercices_auto(ref,nb,path,exo_ordonne,comp,consigne,dollar=False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
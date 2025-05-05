from random import *
from Exerciseur import *

ref="CalcAntecedent" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=12 # Le nombre d'exercice

comp="" # La compétence de l'exercice

consigne="(Calculer) Pour cette exercice, on considère les fonctions $f:x\\mapsto 2x+4$, $g:x\\mapsto 4x^2-2$ et $h:x\\mapsto \\dfrac{1}{x}$" #La consigne générale

path="Ex_Calculer/Exo_DonnerAntecedent.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

list_fonction=["$f","$g","$h"]

list_alea=[]
for index in range(nb):
    f=randint(0,2)
    if f==1:
        i=randint(-9,9)**2+2
    elif f==2:
        i=randint(1,10)*(-1)**2
    else :
        i=randint(-15,15)
    while [f,i] in list_alea:
        f=randint(0,2)
        if f==1:
            i=randint(-9,9)**2+2
        elif f==2:
            i=randint(1,10)*(-1)**2
        else :
            i=randint(-15,15)
    list_alea.append([f,i])

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    if index < nb/2:
        exo[index]=list_fonction[list_alea[index][0]]+"(\\fillin[1cm])="+str(list_alea[index][1])+"$"
    else : 
        exo[index]="Les antécédents de "+str(list_alea[index][1])+ " par la fonction "+list_fonction[list_alea[index][0]]+"$ sont \\fillin[1cm]"
        if index>nb-3:
            exo[index]+="\\columnbreak"

echangeur=[0,4,8,1,5,9,2,6,10,3,7,11]
exo_ordonne=list(range(nb))

for index in range(nb):
    exo_ordonne[echangeur[index]]=exo[index]


exercices_auto(ref,nb,path,exo_ordonne,comp,consigne,3,dollar=False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
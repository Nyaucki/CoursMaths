from random import *
from Exerciseur import *
from Make_Tab import *

ref="TabToHisto" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=6 # Le nombre d'exercice

comp="Représenter" # La compétence de l'exercice

consigne="Tracer l'histograme correspondannt à la série" #La consigne générale

path="Ex_Representer/Exo_SerieHisto.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    lst_var=[]
    lst_eff=[]
    lngth=5
    if index>2:
        lngth+=1
    if index>4:
        lngth+=1
    dprt=randint(1,10)
    for i in range(lngth):
        dprt+=randint(1,3)
        lst_var.append(dprt)
        lst_eff.append(randint(1,10))
    exo[index]="\n"+tabu_stat(lst_var,lst_eff)
    

exercices_auto(ref,nb,path,exo,comp,consigne,2,dollar=False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
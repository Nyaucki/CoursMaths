from random import *
from Exerciseur import *
from Make_Diag import *

ref="HistoToTab" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=6 # Le nombre d'exercice

comp="Représenter" # La compétence de l'exercice

consigne="Tracer le tableau de valeurs correspondannt à l'histogramme" #La consigne générale

path="Ex_Representer/Exo_HistoSerie.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    lst_var=[]
    lst_eff=[]
    lngth=4
    if index>2:
        lngth+=1
    if index>4:
        lngth+=1
    dprt=randint(1,10)
    for i in range(lngth):
        dprt+=randint(1,3)
        lst_var.append(dprt)
        lst_eff.append(randint(1,5))
    exo[index]="\n"+diag_mk(lst_var,lst_eff)
    

exercices_auto(ref,nb,path,exo,comp,consigne,2,dollar=False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
from random import *
from Exerciseur import *

ref="Multiple"

nb=12

path="Ex_Calculer/Exo_MultiplesNegations.tex"

exo=list(range(nb))
for index in exo:
    exo[index]=plusmoins() + str(randint(21,99))
    for j in range (index//3 +1):
        exo[index]= plusmoins() + "(" + exo[index] + ")"

exercices_auto(ref,nb,path,exo)

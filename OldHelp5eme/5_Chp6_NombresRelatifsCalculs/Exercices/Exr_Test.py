from random import *
from Exerciseur import *

ref="Test"

nb=20

path="Test.tex"

exo=list(range(nb))
for index in exo:
    exo[index]=plusmoins() + str(randint(1,20))
    for j in range (index//5 +1):
        exo[index]= exo[index] + plusmoins() + "("+plusmoins() + str(randint(1,20))+")"

exercices_auto(ref,nb,path,exo)

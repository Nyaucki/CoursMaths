from random import *
from Exerciseur import *

ref="Trous"

nb=16

path="Ex_Chercher/Exo_CalculsATrous.tex"

exo_plus=list(range(nb//2))
for index in exo_plus:
    a=randint(11,21)*(-1)**randint(0,1)
    b=randint(1,10)*(-1)**randint(0,1)
    exo_plus[index]=str(a)+"+ \\filing ="+str(b)

exo_moins=list(range(nb//2))
for index in exo_moins:
    a=randint(11,21)*(-1)**randint(0,1)
    b=randint(1,10)*(-1)**randint(0,1)
    exo_moins[index]=str(a)+"- \\filing ="+str(b)

exo=exo_plus + exo_moins

exercices_auto(ref,nb,path,exo)

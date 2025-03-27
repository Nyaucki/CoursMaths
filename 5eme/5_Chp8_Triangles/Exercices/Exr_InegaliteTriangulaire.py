from random import *
from Exerciseur import *

ref="InegaliteTriangulaire" # Ce qui servira de référence aux exercices pour le fichier Tex

comp=""

consigne="(Calculer) Les triangles $ABC$ suivants peuvent-ils être tracés ?"

nb=12 # Le nombre d'exercice

path="Ex_Calculer/Exo_InegaliteTriangulaire.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    a=randint(2,5)
    b=randint(2,5)
    c=a+b +(-1)**randint(0,1)*randint(1,3)
    exo[index]="\\begin{itemize}\n\\item $AB="+str(a)+"$ cm\n\\item $AC="+str(b)+"$ cm\n\\item $BC="+str(c)+"$ cm\n\\end{itemize}"

exercices_auto(ref,nb,path,exo,comp,consigne,False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 5eme argumant pour modifier ceci.

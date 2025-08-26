from random import *
from Exerciseur import *

ref="TracerRaporteur" # Ce qui servira de référence aux exercices pour le fichier Tex

comp=""

consigne="(Représenter) Tracer les triangles $ABC$ suivants"

nb=8 # Le nombre d'exercice

path="Ex_Representer/Exo_TracerTriangleRaporteur.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    if index<4:
        a=randint(2,5)
        b=randint(2,5)
        c=randint(13,113)
        exo[index]="\\begin{itemize}\n\\item $AB="+str(a)+"$ cm\n\\item $AC="+str(b)+"$ cm\n\\item $\\widehat{ABC}="+str(c)+"$ °\n\\end{itemize}"
    else :
        a=randint(2,5)
        b=randint(13,113)
        c=180-b-randint(17,43)
        exo[index]="\\begin{itemize}\n\\item $AB="+str(a)+"$ cm\n\\item $\\widehat{BAC}="+str(b)+"$ °\n\\item $\\widehat{ABC}="+str(c)+"$ °\n\\end{itemize}"

exercices_auto(ref,nb,path,exo,comp,consigne,False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 5eme argumant pour modifier ceci.

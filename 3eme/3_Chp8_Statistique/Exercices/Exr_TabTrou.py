from random import *
from Exerciseur import *
from Make_Tab import *
import math

def frac_tex(num,den):
    div=math.gcd(int(num),int(den))
    a=num//div
    b=den//div
    if b ==1:
        return str(int(a))
    else :
        return(str("\\dfrac{"+str(a)+"}{"+str(b)+"}"))

ref="Tab_trou" # Ce qui servira de référence aux exercices pour le fichier Tex

nb=8 # Le nombre d'exercice

comp="Chercher" # La compétence de l'exercice

consigne="Compléter la série pour avoir la bonne moyenne" #La consigne générale

path="Ex_Chercher/Exo_Tableaux_Trous.tex" # Le chemin (relatif suffit) vers le fichier à modifier/ecrire

exo=list(range(nb)) # Le code pour générer les exercices aléatoires
for index in exo:
    lst_var=[]
    lst_eff=[]
    lngth=4
    if index <4 :
        lngth=6
    moy=0
    moy_div=0
    dprt=randint(1,10)
    for i in range(lngth):
        dprt+=randint(1,3)
        lst_var.append(dprt)
        eff=randint(1,10)
        lst_eff.append(eff)
        moy+=dprt
        moy_div+=eff
    if index <4:
        moy_div=lngth
    if i<6 :
        lst_var[randint(0,lngth-1)]="$x$"
    else : 
        lst_eff[randint(0,lngth-1)]="$x$"
    if index<4:
        exo[index]="\n"+str(lst_var).replace("[","").replace("]","").replace("'","")+"   avec $\\overline{x}="+frac_tex(moy,moy_div)+"$"
    else :
        exo[index]="\n"+tabu_stat(lst_var,lst_eff,center=False)+"   avec $\\overline{x}="+frac_tex(moy,moy_div)+"$"

exo[2],exo[4]=exo[4],exo[2]
exo[3],exo[5]=exo[5],exo[3]

exercices_auto(ref,nb,path,exo,comp,consigne,2,dollar=False) # Par défaut, écrit sur 4 colonnes. On peut rajouter un 6eme argument pour modifier ceci.
import os
from MyScripts.Exerciseur import *

def makTrouverDiviseur(nb):
    val = mat_alea(nb,[[1,3],[1,2],[0,1],[0,1]]) # puissance 2 , 3 , 5 , 7 
    txt=["" for _ in range(nb)]
    for qu in range(nb):
        p2=val[qu][0]
        p3=val[qu][1]
        p5=val[qu][2]
        p7=val[qu][3]
        txt[qu]="$$"+str(2**p2*3**p3*5**p5*7**p7)+"$$\n\\dotlines{3}"
    return(txt)


if __name__=="__main__":
    exercices_auto(os.path.dirname(os.path.realpath(__file__)),"TrouverDiviseur", makTrouverDiviseur(6),dolar=False,nb_column=3,consigne="Trouver tous les diviseurs des nombres suivants.")

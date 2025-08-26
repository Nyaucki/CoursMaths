import os
from MyScripts.Exerciseur import *

def makDiviseur(nb):
    val = mat_alea(nb,[[4,9],[21,35],[0,1]]) # diviseur ? , quotient , reste ? 
    txt=["" for _ in range(nb)]
    for qu in range(nb):
        txt[qu]=str(val[qu][0]) +" est il un diviseur de " + str(val[qu][0]*val[qu][1]+val[qu][2]) + " ?\n\\dotlines{0}"
    return(txt)


if __name__=="__main__":
    exercices_auto(os.path.dirname(os.path.realpath(__file__)),"Diviseur", makDiviseur(3),consigne="",dolar=False,nb_column=3)

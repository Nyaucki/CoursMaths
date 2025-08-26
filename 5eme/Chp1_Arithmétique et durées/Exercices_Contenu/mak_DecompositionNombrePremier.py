import os
from MyScripts.Exerciseur import *

def makDecompositionNombrePremier(nb):
    val = mat_alea(nb,[[0,2],[0,2],[0,1],[0,1],[0,1],[0,1]]) # puissance 2 , 3 , 5 , 7 
    txt=["" for _ in range(nb)]
    for qu in range(nb):
        p2=val[qu][0]
        p3=val[qu][1]
        p5=val[qu][2]
        p7=val[qu][3]
        p11=val[qu][4]
        p13=val[qu][5]
        txt[qu]="$$"+str(2**p2*3**p3*5**p5*7**p7*11**p11*13**p13)+"$$"
    return(txt)


if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    name=os.path.basename(__file__).replace(".py","").replace("mak_","") #Automaticaly get the  name of the file
    exercices_auto(path,name, makDecompositionNombrePremier(6),dolar=False,nb_column=3,consigne="A faire sur le cahier. Décomposer les nombres suivants en poduit de nombres premiers.")

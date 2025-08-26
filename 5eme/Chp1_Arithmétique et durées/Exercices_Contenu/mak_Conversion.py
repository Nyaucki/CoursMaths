import os
from MyScripts.Exerciseur import *


def makConversion(nb):
    val = mat_alea(nb,[[3000,30000],[1,1000]]) # conv1 et conv2 
    txt=["" for _ in range(nb)]
    for qu in range(nb):
        txt[qu]=str(val[qu][0])+" s\\dotfill\n\n\\vspace*{1em}\\dotfill\n\n"+str(val[qu][1]/100)+" h\\dotfill\n\n\\vspace*{1em}\\dotfill"
    return(txt)

if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    name=os.path.basename(__file__).replace(".py","").replace("mak_","") #Automaticaly get the  name of the file
    exercices_auto(path,name, makConversion(6),dolar=False,nb_column=3,consigne="Convertir les durées suivantes en heures, mimnutes et secondes.")

import os
from MyScripts.Exerciseur import *


def makAdditionnerDurees(nb):
    val = mat_alea(nb,[[10,15],[25,59],[25,59],[1,9],[25,59],[25,59]]) # h1,min1,s1,h2,min2,s2
    txt=["" for _ in range(nb)]
    for qu in range(nb):
        txt[qu]=str(val[qu][0])+"\\text{h }"+str(val[qu][1])+"\\text{min }"+str(val[qu][2])+"\\text{s }~"+plusmoins(qu)+"~"+ str(val[qu][3])+"\\text{h }"+str(val[qu][4])+"\\text{min }" +str(val[qu][5])+"\\text{s }"
    return(txt)

if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    name=os.path.basename(__file__).replace(".py","").replace("mak_","") #Automaticaly get the  name of the file
    exercices_auto(path,name, makAdditionnerDurees(6),dolar=True,nb_column=3,consigne="A faire sur le cahier. Effectuer les opérations suivantes sur les durées")

from random import *

def plusmoins() -> str:
        if randint(0,2)==0:
            return("+")
        else:
            return("-")


def exercices_auto(ref : str,nb_exo : int,path : str,exo : list,comp : str, consigne ="",dolar=True,nb_column = 4) -> None:
    with open(path,"w") as fichier :
        fichier.write("\\consigne{"+ ref + "1}{" + ref + str(nb_exo)+"} "+consigne+"\n\n")
        fichier.write("\\begin{multicols}{"+str(nb_column)+"}\n")
        for index in range(nb_exo):
            fichier.write("\\exo{"+ comp +"}{"+ref+str(index +1 )+"} \n")
            if dolar :
                fichier.write("$$"+exo[index]+"$$\n\n")
            else :
                 fichier.write(exo[index]+"\n\n")
        fichier.write("\\end{multicols}")

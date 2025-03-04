from random import *

def plusmoins() -> str:
        if randint(0,2)==0:
            return("+")
        else:
            return("-")


def exercices_auto(ref : str,nb_exo : int,path : str,exo : list, nb_column = 4) -> None:
    with open(path,"w") as fichier :
        fichier.write("\\consigne{"+ ref + "1}{" + ref + str(nb_exo)+"}\n\n")
        fichier.write("\\begin{multicols}{nb_column}\n")
        for index in range(nb_exo):
            fichier.write("\exo{Calculer}{"+ref+str(index +1 )+"}\\\\ \n")
            fichier.write(exo[index]+"\n\n")
        fichier.write("\\end{multicols}")

from random import *

def plusmoins():
        if randint(0,2)==0:
            return("+")
        else:
            return("-")


def exercices_auto(ref,nb,path,exo):

    with open(path,"w") as fichier :
        fichier.write("\\consigne{"+ ref + "1}{" + ref + str(nb)+"}\n\n")
        fichier.write("\\begin{multicols}{4}\n")
        for index in range(nb):
            fichier.write("\exo{Calculer}{"+ref+str(index +1 )+"}\\\\ \n")
            fichier.write(exo[index]+"\n\n")
        fichier.write("\\end{multicols}")

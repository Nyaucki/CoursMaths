import os
from MyScripts.Labyrinthe import * 

if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    name=os.path.basename(__file__).replace(".py","").replace("mak_","") #Automaticaly get the  name of the file
    valDepart=92
    def funcplus(val):
        return(val+randint(2,23))
    def funcmoins(val):
        return(val-randint(2,23))
    def finish(i,j,val):
        if (i+j)%2==0:
            return(str(val)+"s")
        else :
            return(str(int(100*val/60)/100)+"min")

    labyrinthe(path=path,name=name,consigne="Traverser le labyrinthe en franchissant les cases dans l'ordre croissant ",valDepart=valDepart,funcplus=funcplus,funcmoins=funcmoins,finish=finish,scale=1.7)

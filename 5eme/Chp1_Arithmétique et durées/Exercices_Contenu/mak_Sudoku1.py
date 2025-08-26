import os
from MyScripts.Sudoku import *

def func(reste):
    d=max(int(reste)+randint(1,2),randint(3,11))
    return(str(int(reste)+d*randint(111,9999))+"\\div"+str(d))

if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    name=os.path.basename(__file__).replace(".py","").replace("mak_","") #Automaticaly get the  name of the file
    listval=denlist(path,name)
    sudoku(path,name,listval,func)


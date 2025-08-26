import os
from MyScripts.Pyramides import *

if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    name=os.path.basename(__file__).replace(".py","").replace("mak_","") #Automaticaly get the  name of the file
    pyramide(path,name,[[" "],[" "," "],[" "," ","2min 05s"],["1min 22s","41s","37s",""]],scale=1.05) # Si pas d'espace dans le premier "", la case est sautée.
    pyramide(path,"corr_"+name,[["6min 44s"],["3min 21s","3min 23s"],["2min 03s","1min 18s","2min 05s"],["1min 22s","41s","37s","1min 28s"]]) # Si pas d'espace dans le premier "", la case est sautée.


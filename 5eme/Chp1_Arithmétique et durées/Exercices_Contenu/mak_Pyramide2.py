import os
from MyScripts.Pyramides import *

if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    name=os.path.basename(__file__).replace(".py","").replace("mak_","") #Automaticaly get the  name of the file
    pyramide(path,name,[["2h 1s"],["1h 4min 2s"," "],[" ","39min 1s"," "],["15min 2s"," "," ","10min 59s"]],scale=1.05) # Si pas d'espace dans le premier "", la case est sautée.
    pyramide(path,"corr_"+name,[["2h 1s"],["1h 4min 2s","55min 59s"],["25min 1s","39min 1s","16min 58s"],["15min 2s","9min 59s","29min 2s","10min 59s"]]) # Si pas d'espace dans le premier "", la case est sautée.


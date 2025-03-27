import os

Chemin=os.path.dirname(os.path.realpath(__file__)).split("/")

Dir=Chemin[len(Chemin)-1] 

os.rename("X_ChpY_Act_Truc.tex",Dir+".tex") #Rename dossier act
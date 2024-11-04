import os

Chemin=os.path.dirname(os.path.realpath(__file__)).split("/")

Dir=Chemin[len(Chemin)-1] 

classe=Dir.split("_")[0]

chpnum="Chp" + Dir.split("_")[1]

base=classe + "_" + chpnum

os.rename("Activite/X_ChpY_Act_Truc","Activite/"+ base +"_Act_Truc") #Rename dossier act

os.rename("Cours/X_ChpY_cours.tex","Cours/"+ base + "_cours.tex")#Rename cours./main

os.rename("Exercices/X_ChpY_exo.tex","Exercices/"+ base + "_exo.tex")#Rename exo./main
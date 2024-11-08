import os

Chemin_brut=os.path.dirname(os.path.realpath(__file__))

Chemin=Chemin_brut.split("/")

Dir=Chemin[len(Chemin)-1] 

classe=Dir.split("_")[0]

chpnum=Dir.split("_")[1]

base=classe + "_" + chpnum

os.rename("Activite/X_ChpY_Act_Truc","Activite/"+ base +"_Act_Truc") #Rename dossier act

os.rename("Cours/X_ChpY_cours.tex","Cours/"+ base + "_cours.tex")#Rename cours./main

os.rename("Exercices/X_ChpY_exo.tex","Exercices/"+ base + "_exo.tex")#Rename exo./main

code_a_remplacer = open("Devoirs/DM_X/CreationTest.py").read()

code_a_remplacer=code_a_remplacer.replace("/X","/" + classe)

code_a_remplacer=code_a_remplacer.replace("chemin","/" + Chemin_brut)

with open("Devoirs/DM_X/CreationTest.py","w") as fichier :
    fichier.write(code_a_remplacer)
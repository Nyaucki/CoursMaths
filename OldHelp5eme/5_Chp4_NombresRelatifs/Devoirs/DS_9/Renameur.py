##### A utiliser après avoir rempli la classe dans le switches.tex et renommer le dossier ######

import os

Chemin=os.path.dirname(os.path.realpath(__file__)).split("/")

Dir=Chemin[len(Chemin)-1] 

DSnum=Dir.split("_")[1]

lign_classe=""

with open("Switches.tex", 'r') as file:
        for line in file:
            if "\\classe" in line:
                lign_classe=lign_classe+line

classe=lign_classe.split("}")[1]
classe=classe.replace('{','')

os.rename("Y_X.tex",classe + "_DS"+ DSnum+".tex") #Rename dossier act

with open("Y_X.tex", 'w') as file:
     file.write("\\documentclass[12pt,a4paper,french,fleqn]{/home/nyaucki/Documents/Prof/CoursMaths/mycls/interro}\n\n\\begin{document}\n\n\\input{Switches}\n\n\\include{Texte}\n\n\\end{document}")

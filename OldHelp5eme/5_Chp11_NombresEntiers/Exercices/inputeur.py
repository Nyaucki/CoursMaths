import os

directories=["Ex_Calculer","Ex_Chercher","Ex_Communiquer","Ex_Durs","Ex_Modeliser","Ex_Raisonner","Ex_Representer"]

Liste_Exo,Liste_Corr="\\section*{\\titre- Exercices}\n\n","\\section*{\\titre- Correction}\n\n"

for directory in directories:
        for filename in os.listdir(directory):
            if filename.startswith('Exo'):
                Liste_Exo=Liste_Exo+"\\input{"+directory+"/"+ filename+"}\n\n"
            elif filename.startswith('Corr'):
                Liste_Corr=Liste_Corr+"\\input{"+directory+"/"+ filename+"}\n\n"

with open("Mode_Impression/Eleves.tex","w") as fichier :
    fichier.write(Liste_Exo)

with open("Mode_Impression/Corrections.tex","w") as fichier :
    fichier.write(Liste_Corr)

with open("Mode_Impression/Texte.tex","w") as fichier :
    fichier.write(Liste_Exo)
    fichier.write("\\newpage \n\n")
    fichier.write(Liste_Corr)

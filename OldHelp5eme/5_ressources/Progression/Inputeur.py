import os

directory="Chapitres"

code=""
with open("Texte.tex","w") as fichier :
    fichier.write("\\foreach \\titre in {\n")
    for filename in os.listdir(directory):
        code+=filename.replace(".tex","") + ",\n"
    fichier.write(code[:-2])
    fichier.write("\n}\n{\\section{\\titre}\n\\input{Chapitres/\\titre}}")
    

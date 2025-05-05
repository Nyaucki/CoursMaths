import os

directory="Cours"


with open("Texte.tex","w") as fichier :
    fichier.write("\\maketitle \\vspace*{-5em}\n\n")
    for filename in os.listdir(directory):
        fichier.write("\\input{Cours/"+ filename+"}\n\n")
    


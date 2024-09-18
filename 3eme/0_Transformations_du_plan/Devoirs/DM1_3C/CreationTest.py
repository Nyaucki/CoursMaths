#!/usr/bin/env python3
import os
import random


liste = open("/home/nyaucki/Documents/Prof/CoursMaths/3eme/ressources/ListeEleves3C.csv","r")
listeNoms = liste.read()
listeNoms = listeNoms.split('\n')
listeNoms.remove('')

noms,prenoms=[],[]
for paire in listeNoms:
    y = paire.split(',')
    #y.remove('')
    noms.append(y[0])
    prenoms.append(y[1])

    
liste.close()

code_a_remplacer = open("Sujet0.tex").read()

with open("SujetEntier.tex","w") as fichier :
    fichier.write("\\documentclass{activite}\n\\usepackage{tabularx}\n\\usepackage{pythontex}\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{document}\n")
    for i in range(len(noms)):
        code = code_a_remplacer.replace('\\nom',noms[i] + ' ' + prenoms[i])
        code = code.replace('\\prenom',prenoms[i])
        fichier.write(code)
        fichier.write('\n')
        fichier.write('\\newpage\n')
    fichier.write('\\end{document}')


os.system('make')

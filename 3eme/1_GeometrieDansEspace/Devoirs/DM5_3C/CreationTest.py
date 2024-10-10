#!/usr/bin/env python3
import os
from random import *

seed_numb=666

liste = open("/home/nyaucki/Documents/Prof/CoursMaths/3eme/ressources/ListeEleves3C.csv","r")
listeNoms = liste.read()
listeNoms = listeNoms.split('\n')

noms,prenoms=[],[]
for paire in listeNoms:
    y = paire.split(',')
    #y.remove('')
    noms.append(y[0])
    prenoms.append(y[1])

def div10(a): #Pour éviter les nombres divisibles par 10
    if a%10==0 :
        a=a+randint(1,9)
    return(a)

liste.close()

code_a_remplacer = open("Sujet0.tex").read()

seed(seed_numb)

with open("SujetEntier.tex","w") as fichier :
    fichier.write("\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/DevoirMaison}\n\\usepackage{tabularx}\n\\usepackage{pythontex}\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{document}\n\\input{Switch.tex}\n")
    for i in range(len(noms)):
        print(noms[i] + ' ' + prenoms[i])
        code_sujet = code_a_remplacer.replace('\\nom}{}','\\nom}{' + noms[i] + ' ' + prenoms[i] +'}') #Remplace les noms
        code_sujet = code_sujet.replace('\\prenom}{}','\\prenom}{' + prenoms[i] + '}')
        code_sujet = code_sujet.replace('\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/DevoirMaison}','') #Retire le documentclass
        code_sujet = code_sujet.replace('\\begin{document}','') #Retire le begin document
        code_sujet = code_sujet.replace('\\end{document}','') #Retire le begin document
        ##### Question a #####
        aun = randint(2,9)
        code_sujet = code_sujet.replace('\\aun',str(aun))
        adeux = randint(2,9)
        code_sujet = code_sujet.replace('\\adeux',str(adeux))
        atrois = randint(2,9)
        code_sujet = code_sujet.replace('\\atrois',str(atrois))
        ##### Question b #####
        bun = randint(2,9)
        code_sujet = code_sujet.replace('\\bun',str(bun))
        bdeux = randint(2,9)
        code_sujet = code_sujet.replace('\\bdeux',str(bdeux))
        ##### Question c #####
        cun = randint(2,9)
        code_sujet = code_sujet.replace('\\cun',str(cun))
        cdeux = randint(2,9)
        code_sujet = code_sujet.replace('\\cdeux',str(cdeux))
        ##### Question d #####
        dun = randint(2,9)
        code_sujet = code_sujet.replace('\\dun',str(dun))
        ddeux = randint(2,9)
        code_sujet = code_sujet.replace('\\ddeux',str(ddeux))
        fichier.write(code_sujet)
        fichier.write('\n')
        if i%2==0 :
            fichier.write('\\vfill')
        else :
            fichier.write('\\newpage\n')
    fichier.write('\\end{document}')


os.system('make')

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
        un = div10(randint(11,1000))
        code_sujet = code_sujet.replace('\\un',str(un))
        deux = div10(randint(100,10000))/10000
        code_sujet = code_sujet.replace('\\deux',str(deux))
        trois = div10(randint(1,1000))
        code_sujet = code_sujet.replace('\\trois',str(trois))
        quatre = randint(1,1000)+randint(1,1000)/1000
        code_sujet = code_sujet.replace('\\quatre',str(quatre))
        fichier.write(code_sujet)
        fichier.write('\n')
        if i%2==0 :
            fichier.write('\\vfill')
        else :
            fichier.write('\\newpage\n')
    fichier.write('\\end{document}')


os.system('make')

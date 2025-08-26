#!/usr/bin/env python3
import os
from random import *

def Creation(classe,seed_numb):
    path="/home/nyaucki/Documents/Prof/CoursMaths/5eme/5_ressources/ListeEleve" + classe + ".csv"

    liste = open(path,"r")
    listeNoms = liste.read()
    listeNoms = listeNoms.split('\n')

    noms,prenoms=[],[]
    for paire in listeNoms:
        y = paire.split(',')
        #y.remove('')
        noms.append(y[0])
        prenoms.append(y[1])

    liste.close()

    code_a_remplacer = open("Sujet0.tex").read()

    seed(seed_numb)

    with open(classe +"_DM_14_SujetEntier.tex","w") as fichier :
        fichier.write("\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/DevoirMaison}\n\\usepackage{tabularx}\n\\usepackage{pythontex}\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{document}\n\\input{//home/nyaucki/Documents/Prof/CoursMaths/5eme/5_Chp7_FractionIntroduction/Devoirs/DM_14/Switch.tex}\n\\renewcommand{\classe}{"+classe+"}\n")
        for i in range(len(noms)):
            code_sujet = code_a_remplacer.replace('\\nom}{}','\\nom}{' + noms[i] + ' ' + prenoms[i] +'}') #Remplace les noms
            code_sujet = code_sujet.replace('\\prenom}{}','\\prenom}{' + prenoms[i] + '}')
            code_sujet = code_sujet.replace('\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/DevoirMaison}','') #Retire le documentclass
            code_sujet = code_sujet.replace('\\begin{document}','') #Retire le begin document
            code_sujet = code_sujet.replace('\\end{document}','') #Retire le end document
            ##### Question a #####
            dena=randint(101,199)
            Qu_A=[dena,randint(101,199),dena]
            for index,var in enumerate(Qu_A):
                code_sujet = code_sujet.replace('\\a'+str(index+1),str(var))
            ##### Question b #####
            denb=randint(3,10)
            Qu_B=[denb*randint(3,10),randint(3,10),denb]
            for index,var in enumerate(Qu_B):
                code_sujet = code_sujet.replace('\\b'+str(index+1),str(var))
            ##### Question c #####
            denc=randint(3,10)
            Qu_C=[denc*randint(3,10),randint(3,10),denc]
            for index,var in enumerate(Qu_C):
                code_sujet = code_sujet.replace('\\c'+str(index+1),str(var))
            ##### Question d #####
            dend=randint(3,10)
            Qu_D=[dend*randint(3,10),randint(3,10),dend]
            for index,var in enumerate(Qu_D):
                code_sujet = code_sujet.replace('\\d'+str(index+1),str(var))
            fichier.write(code_sujet)
            if i%2==0:
                fichier.write('\\vfil\n')
            else:
                fichier.write('\\newpage\n')
        fichier.write('\\end{document}')


if __name__ == '__main__':
    Creation('3C',666)

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

    with open(classe+"/SujetEntier" + classe +".tex","w") as fichier :
        fichier.write("\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/DevoirMaison}\n\\usepackage{tabularx}\n\\usepackage{pythontex}\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{document}\n\\input{/home/nyaucki/Documents/Prof/CoursMaths/5eme/5_Chp4_NombresRelatifs/Devoirs/DM8/Switch.tex}\n\\renewcommand{\classe}{"+classe+"}\n")
        for i in range(len(noms)):
            code_sujet = code_a_remplacer.replace('\\nom}{}','\\nom}{' + noms[i] + ' ' + prenoms[i] +'}') #Remplace les noms
            code_sujet = code_sujet.replace('\\prenom}{}','\\prenom}{' + prenoms[i] + '}')
            code_sujet = code_sujet.replace('\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/DevoirMaison}','') #Retire le documentclass
            code_sujet = code_sujet.replace('\\begin{document}','') #Retire le begin document
            code_sujet = code_sujet.replace('\\end{document}','') #Retire le end document
            ##### Question a #####
            Qu_A=[randint(301,399)/100,randint(301,399)/100]
            for index,var in enumerate(Qu_A):
                code_sujet = code_sujet.replace('\\a'+str(index+1),str(var))
            ##### Question b #####
            Qu_B=[randint(401,499)/1000,randint(401,499)/1000]
            for index,var in enumerate(Qu_B):
                code_sujet = code_sujet.replace('\\b'+str(index+1),str(var))
            ##### Question c #####
            Qu_C=[randint(31,39)/10,randint(301,399)/100]
            for index,var in enumerate(Qu_C):
                code_sujet = code_sujet.replace('\\c'+str(index+1),str(var))
            ##### Question d #####
            Qu_D=[randint(71,79)/100,randint(701,799)/1000]
            for index,var in enumerate(Qu_D):
                code_sujet = code_sujet.replace('\\d'+str(index+1),str(var))
            ##### Question e #####
            Qu_E=[randint(2001,2999)/1000,randint(201,299)]
            for index,var in enumerate(Qu_E):
                code_sujet = code_sujet.replace('\\e'+str(index+1),str(var))
            ##### Question f #####
            Qu_F=[randint(11,99)/1000,randint(1,99)]
            for index,var in enumerate(Qu_F):
                code_sujet = code_sujet.replace('\\f'+str(index+1),str(var))
            ##### Question g #####
            Qu_G=[randint(31,39),randint(301,399)]
            for index,var in enumerate(Qu_G):
                code_sujet = code_sujet.replace('\\g'+str(index+1),str(var))
            ##### Question h #####
            Qu_H=[randint(71,79),randint(701,799)]
            for index,var in enumerate(Qu_H):
                code_sujet = code_sujet.replace('\\h'+str(index+1),str(var))
            fichier.write(code_sujet)
            if i%3==2:
                fichier.write('\\newpage\n')
            else :
                fichier.write('\\vfill\n')
        fichier.write('\\end{document}')


    os.system('make')

if __name__ == '__main__':
    Creation('5E',666)
#!/usr/bin/env python3
import os
from random import *

def Creation(classe,seed_numb):
    path="/home/nyaucki/Documents/Prof/CoursMaths/5eme/ressources/ListeEleve" + classe + ".csv"

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
        fichier.write("\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/DevoirMaison}\n\\usepackage{tabularx}\n\\usepackage{pythontex}\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{document}\n\\input{/home/nyaucki/Documents/Prof/CoursMaths/5eme/1_RappelsPriorités/Devoirs/DM5/Switch.tex}\n\\renewcommand{\classe}{"+classe+"}\n")
        for i in range(len(noms)):
            code_sujet = code_a_remplacer.replace('\\nom}{}','\\nom}{' + noms[i] + ' ' + prenoms[i] +'}') #Remplace les noms
            code_sujet = code_sujet.replace('\\prenom}{}','\\prenom}{' + prenoms[i] + '}')
            code_sujet = code_sujet.replace('\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/DevoirMaison}','') #Retire le documentclass
            code_sujet = code_sujet.replace('\\begin{document}','') #Retire le begin document
            code_sujet = code_sujet.replace('\\end{document}','') #Retire le end document
            #Question A
            aun = randint(1,10)
            code_sujet = code_sujet.replace('\\aun',str(aun))
            adeux = randint(3,9)
            code_sujet = code_sujet.replace('\\adeux',str(adeux))
            atrois = randint(3,9)
            code_sujet = code_sujet.replace('\\atrois',str(atrois))
            aquatre = randint(1,9)
            code_sujet = code_sujet.replace('\\aquatre',str(aquatre))
            #Question B
            bun = randint(1,5)
            code_sujet = code_sujet.replace('\\bun',str(bun))
            bdeux = randint(1,5)
            code_sujet = code_sujet.replace('\\bdeux',str(bdeux))
            btrois = randint(6,14)
            code_sujet = code_sujet.replace('\\btrois',str(btrois))
            bquatre = randint(4,5)
            code_sujet = code_sujet.replace('\\bquatre',str(bquatre))
            #Question C
            cun = randint(1,3)
            code_sujet = code_sujet.replace('\\cun',str(cun))
            cdeux = randint(1,3)
            code_sujet = code_sujet.replace('\\cdeux',str(cdeux))
            ctrois = 12-cun * cdeux
            code_sujet = code_sujet.replace('\\ctrois',str(ctrois))
            cquatre = randint(2,4)
            code_sujet = code_sujet.replace('\\cquatre',str(cquatre))
            #Question D
            dun = randint(1,10)
            code_sujet = code_sujet.replace('\\dun',str(dun))
            ddeux = randint(6,12)
            code_sujet = code_sujet.replace('\\ddeux',str(ddeux))
            dtrois = randint(2,5)
            code_sujet = code_sujet.replace('\\dtrois',str(dtrois))
            dquatre = randint(1,10)
            code_sujet = code_sujet.replace('\\dquatre',str(dquatre))
            dcinq = randint(1,10)
            code_sujet = code_sujet.replace('\\dcinq',str(dcinq))
            fichier.write(code_sujet)
            fichier.write('\n')
            if i%2==0 :
                fichier.write('\\vfill')
            else :
                fichier.write('\\newpage\n')
        fichier.write('\\end{document}')


    os.system('make')

if __name__ == '__main__':
    Creation('5E',666)
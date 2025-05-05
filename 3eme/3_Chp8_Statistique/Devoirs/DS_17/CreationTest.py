#!/usr/bin/env python3
import os
from random import *
import math

def frac_tex(num,den):
    div=math.gcd(int(num),int(den))
    a=num//div
    b=den//div
    if b ==1:
        return str(int(a))
    else :
        return(str("\\dfrac{"+str(a)+"}{"+str(b)+"}"))

def Creation(classe,seed_numb):
    path="/home/nyaucki/Documents/Prof/CoursMaths/3eme/3_ressources/ListeEleve" + classe + ".csv"

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



    seed(seed_numb)

    with open(classe +"_DS_17_SujetEntier.tex","w") as fichier :
        fichier.write("\\documentclass[12pt,a4paper,french,fleqn]{/home/nyaucki/Documents/Prof/CoursMaths/mycls/interro}\n\\begin{document}\n\\input{Switches.tex}\\input{variable.tex}\n\\renewcommand{\\classe}{"+classe+"}\n")
        for i in range(len(noms)):
            fichier.write("\\input{entete.tex}\n\n")
            # Exercice 1
            lst_var=[]
            lst_eff=[]
            med=randint(4,5)
            lngth=4
            dprt=randint(1,10)
            for i in range(lngth):
                dprt+=randint(1,3)
                lst_var.append(dprt)
            a=randint(1,2)
            eff=a
            ecc=eff
            lst_eff.append(eff)
            eff=1
            if a==1:
                eff=2
            ecc+=eff
            lst_eff.append(eff)
            lst_eff.append(med-ecc)
            lst_eff.append(med)
            # Valeurs
            fichier.write("\\renewcommand{\\exAvA}{"+str(lst_var[0])+"}\n")
            fichier.write("\\renewcommand{\\exAvB}{"+str(lst_var[1])+"}\n")
            fichier.write("\\renewcommand{\\exAvC}{"+str(lst_var[2])+"}\n")
            fichier.write("\\renewcommand{\\exAvD}{"+str(lst_var[3])+"}\n")
            # Effectif
            fichier.write("\\renewcommand{\\exAvE}{"+str(lst_eff[0])+"}\n")
            fichier.write("\\renewcommand{\\exAvF}{"+str(lst_eff[1])+"}\n")
            fichier.write("\\renewcommand{\\exAvG}{"+str(lst_eff[2])+"}\n")
            fichier.write("\\renewcommand{\\exAvH}{"+str(lst_eff[3])+"}\n")
            # Exercice 2
            lst_var=[]
            lst_eff=[]
            med=randint(4,5)
            lngth=4
            dprt=randint(1,10)
            for i in range(lngth):
                dprt+=randint(1,3)
                lst_var.append(dprt)
            a=randint(1,2)
            eff=a
            ecc=eff
            lst_eff.append(eff)
            eff=1
            if a==1:
                eff=2
            ecc+=eff
            lst_eff.append(eff)
            lst_eff.append(med-ecc)
            lst_eff.append(med -1)
            # Valeurs
            fichier.write("\\renewcommand{\\exBvA}{"+str(lst_var[0])+"}\n")
            fichier.write("\\renewcommand{\\exBvB}{"+str(lst_var[1])+"}\n")
            fichier.write("\\renewcommand{\\exBvC}{"+str(lst_var[2])+"}\n")
            fichier.write("\\renewcommand{\\exBvD}{"+str(lst_var[3])+"}\n")
            # Effectif
            fichier.write("\\renewcommand{\\exBvE}{"+str(lst_eff[0])+"}\n")
            fichier.write("\\renewcommand{\\exBvF}{"+str(lst_eff[1])+"}\n")
            fichier.write("\\renewcommand{\\exBvG}{"+str(lst_eff[2])+"}\n")
            fichier.write("\\renewcommand{\\exBvH}{"+str(lst_eff[3])+"}\n")
            # Exercice 3
            lst_var=[]
            lst_eff=[]
            med=randint(11,15)
            lngth=4
            dprt=randint(1,10)
            for i in range(lngth):
                dprt+=randint(1,3)
                lst_var.append(dprt)
                lst_eff.append(randint(1,3))
            moy_num=lst_var[0]*lst_eff[0]+lst_var[1]*lst_eff[1]+lst_var[2]*lst_eff[2]+lst_var[3]*lst_eff[3]
            moy_div=lst_eff[0]+lst_eff[1]+lst_eff[2]+lst_eff[3]
            # Valeurs
            fichier.write("\\renewcommand{\\exCvA}{"+str(lst_var[0])+"}\n")
            fichier.write("\\renewcommand{\\exCvB}{"+str(lst_var[1])+"}\n")
            fichier.write("\\renewcommand{\\exCvC}{"+str(lst_var[2])+"}\n")
            fichier.write("\\renewcommand{\\exCvD}{"+str(lst_var[3])+"}\n")
            # Effectif
            fichier.write("\\renewcommand{\\exCvE}{"+str(lst_eff[0])+"}\n")
            fichier.write("\\renewcommand{\\exCvF}{"+str(lst_eff[1])+"}\n")
            fichier.write("\\renewcommand{\\exCvG}{"+str(lst_eff[2])+"}\n")
            fichier.write("\\renewcommand{\\exCvH}{$x$}\n")
            fichier.write("\\renewcommand{\\exCvI}{"+frac_tex(moy_num,moy_div)+"}\n")
            # Exercice 4
            lst_var=[]
            lst_eff=[]
            med=randint(11,15)
            lngth=6
            for i in range(lngth):
                lst_var.append(randint(0,20))
                lst_eff.append(randint(1,3))
            fichier.write("\\renewcommand{\\exDvA}{"+str(lst_var[0])+"}\n")
            fichier.write("\\renewcommand{\\exDvB}{"+str(lst_eff[0])+"}\n")
            fichier.write("\\renewcommand{\\exDvC}{"+str(lst_var[4])+"}\n")
            fichier.write("\\renewcommand{\\exDvD}{"+str(lst_eff[1])+"}\n")
            fichier.write("\\renewcommand{\\exDvE}{"+str(lst_var[2])+"}\n")
            fichier.write("\\renewcommand{\\exDvF}{"+str(lst_eff[2])+"}\n")
            fichier.write("\\renewcommand{\\exDvG}{"+str(lst_var[3])+"}\n")
            fichier.write("\\renewcommand{\\exDvH}{"+str(lst_eff[3])+"}\n")
            fichier.write("\\renewcommand{\\exDvI}{"+str(lst_var[4])+"}\n")
            fichier.write("\\renewcommand{\\exDvJ}{"+str(lst_eff[4])+"}\n")
            fichier.write("\\renewcommand{\\exDvD}{"+str(lst_var[5])+"}\n")
            fichier.write("\\renewcommand{\\exDvE}{"+str(lst_eff[5])+"}\n")
            # Exercice 5
            med =randint(20,100)
            moy=med+(-1)**randint(0,1)*randint(2,5)
            fichier.write("\\renewcommand{\\exEvA}{"+str(randint(10,20))+"}\n")
            fichier.write("\\renewcommand{\\exEvB}{"+str(moy)+"}\n")
            fichier.write("\\renewcommand{\\exEvC}{"+str(med)+"}\n\n")
            fichier.write('\\input{Sujet0.tex}\n\\newpage\n\\setcounter{exrcntr}{0}\n\n')
        fichier.write('\\end{document}')


if __name__ == '__main__':
    Creation('3C',666)

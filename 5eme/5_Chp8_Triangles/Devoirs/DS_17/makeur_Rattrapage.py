#!/usr/bin/env python3
import os
from random import *

def Creation(nb,seed_numb):

    seed(seed_numb)

    with open("Rattrapage.tex","w") as fichier :
        fichier.write("\\documentclass[12pt,a4paper,french,fleqn]{/home/nyaucki/Documents/Prof/CoursMaths/mycls/interro}\n\n\\begin{document}\n\\input{//home/nyaucki/Documents/Prof/CoursMaths/5eme/5_Chp8_Triangles/Devoirs/DS_17/Switch.tex}\\input{entete.tex}\n\\input{Rattrapage_Variables.tex}")
        for i in range(nb):
            #Exercice1
            code="\\renewcommand{\exunAB}{"+str(randint(2,5)) +"}\n"
            code+="\\renewcommand{\exunAC}{"+str(randint(2,5))+"}\n"
            code+="\\renewcommand{\exunBC}{"+str(randint(2,5))+"}\n"
            code+="\\renewcommand{\exunbAB}{"+str(randint(2,5))+"}\n"
            code+="\\renewcommand{\exunABC}{"+ str(10*randint(2,6))+"}\n"
            code+="\\renewcommand{\exunBAC}{"+str(10*randint(2,6))+"}\n"
            #Exercice2
            dpt=randint(0,3)
            iso=randint(1,9)
            iso2=randint(1,9)
            while iso2==iso:
                iso2=randint(1,9)
            equi=randint(1,9)
            imp1=randint(1,4)
            imp2=randint(1,4)
            while imp2==imp1:
                imp2=randint(1,4)
            imp3=imp1+imp2+randint(1,3)
            lst=[[iso,iso2,iso],[imp1,imp3,imp2],[equi,equi,equi],[randint(1,9),randint(1,9),randint(1,9)]]
            code+="\\renewcommand{\eDqAmA}{"+str(lst[dpt][1])+"}\n"
            code+="\\renewcommand{\eDqAmB}{"+str(lst[dpt][2])+"}\n"
            code+="\\renewcommand{\eDqAmC}{"+str(lst[dpt][0])+"}\n"
            dpt=(dpt+1)%4
            code+="\\renewcommand{\eDqBmA}{"+str(lst[dpt][1])+"}\n"
            code+="\\renewcommand{\eDqBmB}{"+str(lst[dpt][2])+"}\n"
            code+="\\renewcommand{\eDqBmC}{"+str(lst[dpt][0])+"}\n"
            dpt=(dpt+1)%4
            code+="\\renewcommand{\eDqCmA}{"+str(lst[dpt][1])+"}\n"
            code+="\\renewcommand{\eDqCmB}{"+str(lst[dpt][2])+"}\n"
            code+="\\renewcommand{\eDqCmC}{"+str(lst[dpt][0])+"}\n"
            dpt=(dpt+1)%4
            code+="\\renewcommand{\eDqDmA}{"+str(lst[dpt][1])+"}\n"
            code+="\\renewcommand{\eDqDmB}{"+str(lst[dpt][2])+"}\n"
            code+="\\renewcommand{\eDqDmC}{"+str(lst[dpt][0])+"}\n"
            #
            dpt=randint(0,3)
            iso=randint(11,88)
            rect=randint(3,44)
            rect2=90-rect
            imp1=randint(40,90)
            imp2=200+randint(1,23)-imp1
            lst=[[60,60],[rect,rect2],[iso,iso],[imp1,imp2]]
            code+="\\renewcommand{\eDqEmA}{"+str(lst[dpt][1])+"}\n"
            code+="\\renewcommand{\eDqEmB}{"+str(lst[dpt][0])+"}\n"
            dpt=(dpt+1)%4
            code+="\\renewcommand{\eDqFmA}{"+str(lst[dpt][1])+"}\n"
            code+="\\renewcommand{\eDqFmB}{"+str(lst[dpt][0])+"}\n"
            dpt=(dpt+1)%4
            code+="\\renewcommand{\eDqGmA}{"+str(lst[dpt][1])+"}\n"
            code+="\\renewcommand{\eDqGmB}{"+str(lst[dpt][0])+"}\n"
            dpt=(dpt+1)%4
            code+="\\renewcommand{\eDqHmA}{"+str(lst[dpt][1])+"}\n"
            code+="\\renewcommand{\eDqHmB}{"+str(lst[dpt][0])+"}\n"


            code+="\\renewcommand{\eTqAmA}{"+str(randint(1,9))+"}\n"
            code+="\\renewcommand{\eTqAmB}{"+str(randint(1,9))+"}\n"
            code+="\\renewcommand{\eTqAmC}{"+str(randint(1,9))+"}\n"
            code+="\\renewcommand{\eTqAmD}{"+str(randint(1,9))+"}\n"

            code+="\\renewcommand{\eTqBmA}{"+str(randint(1,9))+"}\n"
            code+="\\renewcommand{\eTqBmB}{"+str(randint(1,9))+"}\n"
            code+="\\renewcommand{\eTqBmC}{"+str(randint(1,9))+"}\n"
            code+="\\renewcommand{\eTqBmD}{"+str(randint(1,9))+"}\n"

            code+="\\renewcommand{\eQqAmA}{"+str( randint(30,50))+"}\n"
            code+="\\renewcommand{\eQqAmB}{"+str( randint(30,50))+"}\n"
            code+="\\renewcommand{\eQqAmC}{"+str( randint(30,50))+"}\n"

            code+="\\renewcommand{\eQqBmA}{"+str( randint(30,50))+"}\n"
            code+="\\renewcommand{\eQqBmB}{"+str( randint(30,50))+"}\n"

            code+="\\renewcommand{\eCqAmA}{"+str(randint(2,9) )+"}\n"
            code+="\\renewcommand{\eCqAmB}{"+str(randint(2,9) )+"}\n"
            fichier.write(code)
            fichier.write("\\input{Sujet0.tex}\n\n\\setcounter{exrcntr}{0}\n\n\\newpage")
        fichier.write('\\end{document}')


if __name__ == '__main__':
    Creation(40,666)

import os
from random import *

lettre=["A","B","C","D","E","F","G","H","I"]

def sudoku(path,name,listval,func,abss=lettre): # abss est le nom donné aux abscisses, listval est une liste contenant [[pos0,val0],[pos1,val1],...]
    with open(path+"/"+name+".tex","w") as fichier :
        abssices=""
        for index,val in enumerate(abss):
            abssices+=str(index+1)+"/"+val+","
        fichier.write("\\setlength{\\columnseprule}{0pt}\\begin{minipage}{0.55\\textwidth}\n\\begin{center}\n\t \\begin{tikzpicture}\n\t\t \\draw[thin] (0,0) grid (9,9);\n\t\t \\draw[ultra thick,step=3] (0,0) grid (9,9);\n\t\t \\foreach \\x/\\y in {"+abssices[:-1]+"}\n\t\t\t { \\draw node at (\\x-0.5,-0.5) {\\y};\n\t\t\t \\draw node at (-0.5,\\x-0.5) {\\x}; }")
        fichier.write("\n\t\t \\end{tikzpicture}	\n\t \\end{center}\n\\end{minipage}\n\\hfil\\vrule\\hfil\n\\begin{minipage}{0.4\\textwidth}\n\\begin{itemize}[leftmargin=10pt]\\begin{multicols}{2}\n")
        for val in listval:
            fichier.write("\\item"+str(val[0])+" : "+ str(func(val[1]))+"\n\n")
        if len(listval)%2==1:
            fichier.write("\\item[\\vspace{\\fill}]")
        fichier.write("\\end{multicols}\\end{itemize}\\end{minipage}")


def denlist(path,name,abss=lettre,ords=range(9,0,-1)):
    liste = open(path+"/"+name+".csv","r") # Récupère le contenue du .csv
    listeNoms = liste.read()
    listeNoms = listeNoms.split('\n') # sépare par ligne
    mat=list(range(len(listeNoms[:-1]))) # Permet d'avoir la matrice du sudoku. Le -1 supprime la ligne vide de la fin
    for index,ligne in enumerate(listeNoms[:-1]):
        mat[index]=ligne.split(',') # La liste est maintenant une matrice
    ret=[]
    for i,ligne in enumerate(mat):
        for j,val in enumerate(ligne) :
            if val!="":
                ret.append(["("+str(abss[j])+";"+str(ords[i])+")",val])
    return(ret)

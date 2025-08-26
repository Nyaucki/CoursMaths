import os
from random import randint

def identite(val):
    return(val)

def labyrinthe(path,name,consigne="",valDepart=0,funcplus=identite,funcmoins=identite,finish=identite,scale=2):
    liste = open(path+"/"+name+".csv","r") # Récupère le contenue du .csv
    listeNoms = liste.read()
    listeNoms = listeNoms.split('\n') # sépare par ligne
    mat=list(range(len(listeNoms[:-1]))) # Permet d'avoir la matrice du labyrinthe. Le -1 supprime la ligne vide de la fin
    for index,ligne in enumerate(listeNoms[:-1]):
        mat[index]=ligne.split(',') # La liste est maintenant une matrice
    ############### Pour donner une valeur aux cases touchant le chemin
    for i,ligne in enumerate(mat):
        for j,val in enumerate(ligne) :
            if val=="":
                test=1000
                if str(mat[max(i-1,0)][j]).isdigit(): 
                    test=min(test,int(mat[i-1][j])-0.5)
                if str(mat[min(i+1,len(mat)-1)][j]).isdigit(): 
                    test=min(test,int(mat[i+1][j])-0.5)
                if str(mat[i][max(j-1,0)]).isdigit(): 
                    test=min(test,int(mat[i][j-1])-0.5)
                if str(mat[i][min(j+1,len(mat[i])-1)]).isdigit(): 
                    test=min(test,int(mat[i][j+1])-0.5)
                if test<1000:
                    mat[i][j]=test
    ############### Pour donner les bonnes valeurs aux cases non vides
    sizey=len(mat)
    sizex=len(mat[0])
    listeval=[valDepart]
    for i in range(sizey*sizex): # Overkill, mais permet d'être sûr d'en avoir assez
        listeval.append(funcplus(listeval[i]))
    for i,ligne in enumerate(mat):
        for j,val in enumerate(ligne): # Donner une valeur à toutes les cases
            if val=="":
                if j==0:
                    mat[i][j]=funcmoins(mat[i-1][j])
                else :
                    mat[i][j]=funcmoins(mat[i][j-1])
            elif str(val).isdigit():
                mat[i][j]=listeval[int(val)-1]
            else :
                mat[i][j]=listeval[int(float(val)-0.5)]-randint(2,23)
    ############### La touche finale sur la matrice
    for i,ligne in enumerate(mat):
        for j,val in enumerate(ligne): # Donner une valeur à toutes les cases
            mat[i][j]=finish(i,j,val)    
#################### L'écriture
    with open(path+"/"+name+".tex","w") as fichier :
        fichier.write("\\exo{"+name+"} "+consigne+"\n\n\\begin{center}\n")
        fichier.write("\\tikzmath{\\sizex = "+str(sizex)+" ;\\sizexm=\\sizex-1 ; \\sizey="+str(sizey)+" ; \\sizeym=\\sizey-1;}\n" # 
        +"\\begin{tikzpicture}[scale="+str(scale)+"]\n" #
        +"\t\\foreach \\i in {0,...,\\sizex}\n " #
        +"\t\t{\\foreach \\j in {0,...,\\sizey}\n " #
        +"\t\t\t{\\draw ({max(\\i-0.2,0)},\\j)--({min(\\sizex,\\i+0.2)},\\j);\n" #
        +"\t\t\t\\draw (\\i,{max(0,\\j-0.2)})--(\\i,{min(\\sizey,\\j+0.2)}); }}\n" #
        +"\t\\draw (0,0) rectangle (\\sizex,\\sizey) ;\n" #
        +"\t\\draw[thick,white] (0,\\sizey-0.1)--(0,\\sizeym+0.2) ;\n " #
        +"\t\\draw[thick,white] (\\sizex,0.2)--(\\sizex,0.8) ;\n" #
        +"\t\\draw[-{Latex[length=3mm,width=5mm]}] (-0.5,\\sizey-0.5)--(0,\\sizey-0.5) ;\n" #
        +"\t\\draw[-{Latex[length=3mm,width=5mm]}] (\\sizex,0.5)--(\\sizex+0.5,0.5) ;\n")
        for j,ligne in enumerate(mat):
            for i,val in enumerate(ligne):
                fichier.write("\t\\node at ("+str(i+0.5)+","+str(sizey-j-0.5)+") {"+str(val)+"};\n")
        fichier.write("\\end{tikzpicture}\n\end{center}\n")

if __name__=="__main__":
    print("Hello world")

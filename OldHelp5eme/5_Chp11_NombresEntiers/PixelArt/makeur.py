img=[[2,5,5,5,5,5,2],[5,5,2,2,2,5,5],[5,5,5,5,5,5,5],[3,6,15,6,15,6,3],[6,6,3,3,3,6,6],[2,6,6,6,6,6,2],[5,10,5,5,5,10,5],[5,30,10,10,10,30,5],[15,10,10,10,10,10,15],[2,10,10,10,10,10,2],[2,3,3,2,3,3,2]] #Décris l'image de haut en bas, une liste=une ligne

colour={2:"white",30:"yellow",3:"brown",10:"blue",15:"black",6:"magenta!20",5:"red"} #Associe des couleurs aux nombres 

list_prime=[179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409] #40 nombres premiers d'après wikipédia

def func_mario(val,compt):
    return(val*list_prime[compt])

def row_colour(row,colour):
    result=[]
    for numb in row:
        result.append(colour[numb])
    return result #Permet de remplacer une ligne de nombre par une ligne de couleurs


def pbmaker(name,img,func_exo,colour,folder=""):
    #Partie Solution
    ## Créer le texte
    solution="\\begin{figure}[H]\n\\center\n\\begin{tikzpicture}[scale=0.8]\n\\newcommand{\\y}{0}"
    for row_num,row in enumerate(img):
        solution+="\\renewcommand{\\y}{"+str(-row_num)+"}\n"
        solution+="\\foreach \\x [count=\\xi] in "+str(row_colour(row,colour)).replace("[","{").replace("]","}").replace("'","")+"\n"
        solution+="{\\draw[fill=\\x] (\\xi,\\y) rectangle (\\xi +1,\\y -1);}\n"
    solution+="\\end{tikzpicture}\n\\end{figure}\n"
    ## Créer le fichier
    with open(folder+"solution"+name+".tex","w") as fichier :
        fichier.write(solution)
    # Partie exercice
    ## Définir le compteur de couleurs
    compte_couleur={}
    list_color=[]
    for row in img:
        for color in row:
            if color not in list_color:
                list_color.append(color)
                compte_couleur[color]=0
    ## Obtenir l'image d'exercice
    img_exo=[]
    for row in img:
        row_exo=[]
        for val in row:
            row_exo.append(func_exo(val,compte_couleur[val]))
            compte_couleur[val]+=1
        img_exo.append(row_exo)
    ## Créer le texte
    grid="\\begin{figure}[H]\n\\center\n\\begin{tikzpicture}[scale=0.8]\n\\newcommand{\\y}{0}"
    for row_num,row in enumerate(img_exo):
        grid+="\\renewcommand{\\y}{"+str(-row_num)+"}\n"
        grid+="\\foreach \\x [count=\\xi] in "+str(row).replace("[","{").replace("]","}")+"\n"
        grid+="{\\draw (\\xi,\\y) rectangle (\\xi +1,\\y -1) node[pos=0.5]{{\\scriptsize\\x}};}\n"
    grid+="\\end{tikzpicture}\n\\end{figure}\n"
    ## Créer le fichier
    with open(folder+"exercice"+name+".tex","w") as fichier :
        fichier.write(grid)

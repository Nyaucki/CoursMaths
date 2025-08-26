from pylab import *
import os

def lisseurbw(image): # Convertie image RGB en noir et blanc pur
    img_lisse=[]
    for row in image:
        new_row=[]
        for pix in row:
            if pix[0]<0.5:
                new_row.append(0)
            else:
                new_row.append(255)
        img_lisse.append(new_row)
    return(img_lisse)

colourbw={0:"black",255:"white"} # (pour correction) Associe des couleurs aux nombres 

def row_colour(row,colour):
    result=[]
    for numb in row:
        result.append(colour[numb])
    return result #Permet de remplacer une ligne de nombre par une ligne de couleurs

def pbmaker(path,name,lisseur,func_exo,colour,consigne="",scale=0.8): # Image should have the same name as the mak_ file
    #Partie Solution
    ## Créer le texte
    img=lisseur(imread(path+"/"+name+".png"))
    solution="\\begin{figure}[H]\n\\center\n\\begin{tikzpicture}[scale="+str(scale)+"]\n\\newcommand{\\y}{0}"
    for row_num,row in enumerate(img):
        solution+="\\renewcommand{\\y}{"+str(-row_num)+"}\n"
        solution+="\\foreach \\x [count=\\xi] in "+str(row_colour(row,colour)).replace("[","{").replace("]","}").replace("'","")+"\n"
        solution+="{\\draw[fill=\\x] (\\xi,\\y) rectangle (\\xi +1,\\y -1);}\n"
    solution+="\\end{tikzpicture}\n\\end{figure}\n"
    ## Créer le fichier
    with open(path+"/corr_"+name+".tex","w") as fichier :
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
    grid="\\exo{"+name+"}"+consigne+"\n\n\\begin{figure}[H]\n\\center\n\\begin{tikzpicture}[scale=0.8]\n\\newcommand{\\y}{0}"
    for row_num,row in enumerate(img_exo):
        grid+="\\renewcommand{\\y}{"+str(-row_num)+"}\n"
        grid+="\\foreach \\x [count=\\xi] in "+str(row).replace("[","{").replace("]","}")+"\n"
        grid+="{\\draw (\\xi,\\y) rectangle (\\xi +1,\\y -1) node[pos=0.5]{{\\scriptsize\\x}};}\n"
    grid+="\\end{tikzpicture}\n\\end{figure}\n"
    ## Créer le fichier
    with open(path+"/"+name+".tex","w") as fichier :
        fichier.write(grid)

if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    img=imread(path+"/PixelArt2.png")
    print(lisseurbw(img))

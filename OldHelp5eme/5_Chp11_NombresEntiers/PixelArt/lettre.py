import pylab
from makeur import *

###### Ce script m'a permis de créer les fichier tex associés à chacunes des lettre

def lisseur(image): # Convertie image RGB en noir et blanc pur
    img_lisse=[]
    for row in image:
        new_row=[]
        for pix in row:
            if pix[0]<100:
                new_row.append(0)
            else:
                new_row.append(255)
        img_lisse.append(new_row)
    return(img_lisse)

colour={0:"black",255:"white"} #Associe des couleurs aux nombres 

list_prime=[2,3,5,7,11,13,17,19,23,29,31,37] #Nombre premiers jusqu'à 30

# list_prime=[179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409] #40 nombres premiers difficiles

list_nonprime=[4,6,9,10,15,18,21,25,27,33,35] #12 nompres non premier

# list_nonprime=[183,187,189,195,192,207,209,221,225,230,231,237,239] #12 nompres non premier plus dur


def func_lettre(val,compt):
    if val==0 :
        return(list_prime[compt])
    else :
        return(list_nonprime[compt])


for char in "AZERTYUIOPQSDFGHJKLMWXCVBN":
    img=pylab.imread("Lettre_jpg/"+char+".jpg") #Transforme l'image en une matrice de pixels
    img=lisseur(img) 
    pbmaker(char,img,func_lettre,colour,"Lettre_tex/")

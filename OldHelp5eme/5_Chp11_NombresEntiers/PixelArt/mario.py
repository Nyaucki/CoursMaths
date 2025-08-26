from makeur import *

img=[[2,5,5,5,5,5,2],[5,5,2,2,2,5,5],[5,5,5,5,5,5,5],[3,6,15,6,15,6,3],[6,6,3,3,3,6,6],[2,6,6,6,6,6,2],[5,10,5,5,5,10,5],[5,30,10,10,10,30,5],[15,10,10,10,10,10,15],[2,10,10,10,10,10,2],[2,3,3,2,3,3,2]] #Décris l'image de haut en bas, une liste=une ligne

colour={2:"white",30:"yellow",3:"brown",10:"blue",15:"black",6:"magenta!20",5:"red"} #Associe des couleurs aux nombres 

list_prime=[179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409] #40 nombres premiers d'après wikipédia

def func_mario(val,compt):
    return(val*list_prime[compt])

pbmaker("mario",img,func_mario,colour)
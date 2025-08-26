from random import *

def plusmoins(nb) -> str:
        if nb%2==0:
            return("+")
        else:
            return("-")
            
def frac_tex(num,den):
    div=math.gcd(int(num),int(den))
    a=num//div
    b=den//div
    if b ==1:
        return str(int(a))
    else :
        return(str("\\dfrac{"+str(a)+"}{"+str(b)+"}"))

def mat_alea(nb : int , matrix : list): # nb est le nombre de set à faire, matrix contient les bornes de chaque valeurs.
    vec=["empty" for _ in range(len(matrix))]
    mat=[vec for _ in range(nb+1)] # The +1 ensure that the while loop will always run
    for i in range(nb):
        vec=["empty" for _ in range(len(matrix))]
        while vec in mat:
            for index,val in enumerate(matrix) :
                vec[index]=randint(val[0],val[1])
        mat[i]=vec
    return(mat[:-1]) # Remove the +1 at the end


def exercices_auto(path : str , ref : str,exo : list, consigne ="",dolar=True,nb_column = 4) -> None:
    with open(path+"/"+ref+".tex","w") as fichier :
        fichier.write("\\exo{"+ref+"}"+consigne+"\n")
        fichier.write("\\begin{multicols}{"+str(nb_column)+"}\n")
        for nb,index in enumerate(exo):
            c_break=""
            if (nb + 1) % (len(exo)//nb_column)==0:
                c_break="\\columnbreak"
            if dolar :
                fichier.write("$$"+index+c_break+"$$\n\n")
            else :
                 fichier.write(index+c_break+"\n\n")
        fichier.write("\\end{multicols}")

if __name__=="__main__":
    mat_alea(10,[[2,5],[-32,45],[10,16],[5,8]])

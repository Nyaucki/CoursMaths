import os
from MyScripts.PixelArt import *

list_prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,151,149,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,6007,613,617,619,631,641,643,647,653,659] #120 premiers Nombre premiers


list_nonprime=[4,6,9,10,15,18,21,25,27,33,35,39,42,45,49,51,55,57,60,63,72,75,78,81,85,91,99,102,105,111,119,121,132,134,144,155,158,160,165,171,180,185,190,192,200,183,187,189,195,192,207,209,221,225,230,231,237,240,245,255,258,267,270,273,285,291,299,301,305,310,315,321,324,330,345,343,351,355,363,369,371,380,385,390,400,405,412,420,425,436,440,445,456,462,465,470,471,485,490,495,501,513,522,531,536,545,543,550,560,565,572,590,602,622,633,642,655,645,660] #12 nompres non premier



def func_lettre(val,compt):
    if val==0 :
        return(list_prime[compt])
    else :
        return(list_nonprime[compt])

if __name__=="__main__":
    path=os.path.dirname(os.path.realpath(__file__)) #Automaticaly get the path of the file
    name=os.path.basename(__file__).replace(".py","").replace("mak_","") #Automaticaly get the  name of the file
    consigne="Colorie en noir uniquement les nombres qui ne sont pas premiers."
    pbmaker(path,name,lisseurbw,func_lettre,colourbw,consigne,scale=0.8)

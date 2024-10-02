from random import *

def div10(a): #Pour éviter les nombres divisibles par 10
    if a%10==0 :
        a=a+randint(1,9)
    return(a)
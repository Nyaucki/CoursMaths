import os

Chemin=os.path.dirname(os.path.realpath(__file__)).split("/")

Dir=Chemin[len(Chemin)-1] 

dmnum=Dir.split("_")[1]

code_a_remplacer = open("CreationTest.py").read()

code_a_remplacer=code_a_remplacer.replace("DM_X",Dir)

with open("CreationTest.py","w") as fichier :
    fichier.write(code_a_remplacer)

switch_a_remplacer = open("Switch.py").read()

switch_a_remplacer=switch_a_remplacer.replace("{\\devoirNumero}{X}","{\\devoirNumero}{X"+ dmnum + "}")

with open("Switch.py","w") as fichier :
    fichier.write(switch_a_remplacer)
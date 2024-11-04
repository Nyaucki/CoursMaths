import os
import string


List=[]

with open("Sujet1.tex", 'r') as file:
        for index,line in enumerate(file):
            if "\\exo{" in line:
                List.append(index)

lines = open('Sujet1.tex', 'r').readlines()
baremes=0
cmptc=[]

for index in List:
    x=lines[index].split()
    print(x[0])
    a=x[0].split('}',1)[0]
    a=a.replace('\\exo{','')
    b=x[0].split('}',1)[1]
    b=b.replace('{','')
    b=b.replace('}','')
    baremes=baremes+float(a)
    cmptc.append(b)

with open("comp.tex","w") as fichier :
    fichier.write("\\begin{tabularx}{\\textwidth}{X m{6cm}}\n")
    for comp in cmptc:
         fichier.write("\\textbf{"+comp+"} () & \\compeval \\\\ \n")
    fichier.write("\\end{tabularx} \n \\hrule")
    
NewSwitches=""

with open("Switches.tex", 'r') as file:
        for index,line in enumerate(file): #REplace and work here
            if index==0:
                newline="\\newcommand{\\bareme}{"+ str(int(baremes)) +"} %Bareme du devoir\n"
            else :
                 newline=line
            NewSwitches=NewSwitches+newline

with open("Switches.tex","w") as fichier :
    fichier.write(NewSwitches)



message="VOUS ETES DE FABULEUX ELEVES"

# crée le fichier élève
code=""
for nb,char in enumerate(message.replace(" ","")) :
    code+="\\renewcommand{\\numero}{"+str(nb+1)+"}\n\n\\renewcommand{\\Lettre}{"+char+"}\n\n\\input{Texte}\n\n"
    if nb % 3 ==2:
        code+="\\newpage\n\n"
    else :
        code+="\\vspace*{1ex}\\hrule\\vspace*{-1ex}"

with open("Supertexte.tex","w") as fichier :
        fichier.write(code)

# Crée le fichier prof à projetter
texte="\\begin{center}\n"
nb_space=0
nb_char=0
for nb,char in enumerate(message) :
    if char ==" ":
        nb_space+=1
        if nb_space==1:
            texte+="\\hspace{1cm}\n"
        else :
             texte+="\n\n"
    else :
        nb_char+=1
        texte+="\\begin{tikzpicture}[scale=0.3]\n\\draw (0,0) rectangle (3,4);\n\\draw (0,0) grid (3,4);\n \\node at (1.5,5) {"+str(nb_char)+"};\n \\end{tikzpicture}\n"
texte+="\\end{center}"

with open("SoluceMessage.tex","w") as fichier :
        fichier.write(texte)
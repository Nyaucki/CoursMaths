message="VOUS ETES DE FABULEUX ELEVES"

code=""
for nb,char in enumerate(message.replace(" ","")) :
    code+="\\renewcommand{\\numero}{"+str(nb+1)+"}\n\n\\renewcommand{\\Lettre}{"+char+"}\n\n\\input{Texte}\n\n"
    if nb % 3 ==2:
        code+="\\newpage\n\n"
    else :
        code+="\\vspace*{1ex}\\hrule\\vspace*{-1ex}"

with open("Supertexte.tex","w") as fichier :
        fichier.write(code)
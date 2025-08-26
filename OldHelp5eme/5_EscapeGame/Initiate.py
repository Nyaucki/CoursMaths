text="monsieur loizon vous souhaite d exquises vacances"

lst_lettre=[]
msg=""
esp_cnt=0

for lettre in text:
    if lettre not in lst_lettre:
        lst_lettre.append(lettre)
    msg+="\\remplace"+lettre
    if lettre == " ":
        esp_cnt+=1
        if esp_cnt % 2 ==0 :
            msg+="\n\n"

fa_list=["Baby","Ambulance","Anchor","PiedPiper","Bed","Bell","Bicycle","Bug","Camera","Cube","Plug","Envelope","Gavel","Globe","PuzzlePiece","Key","Lock","Magnet","Map","PaperPlane","Paw"]

txt_associate=""
for idx,lettre in enumerate(lst_lettre):
    txt_associate+="\\newcommand{\\remplace"+lettre +"}{\\fa"+fa_list[idx]+"}\n"

with open("associate.tex","w") as fichier :
    fichier.write(txt_associate)

with open("message_projette.tex","w") as fichier :
    fichier.write("\\documentclass[12pt,a4paper,french,fleqn]{beamer}\n")
    fichier.write("\\usepackage[fixed]{fontawesome5}\n")
    fichier.write("\\begin{document}\n")
    fichier.write("\\input{associate.tex}\n")
    fichier.write("\\begin{frame}\n\\begin{center}\n")
    fichier.write(msg)
    fichier.write("\n\\end{center}\n\\end{frame}\n\\end{document}")

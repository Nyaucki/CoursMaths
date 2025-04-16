def tabu_stat(lst_val,lst_eff,frequence=False,center=True)->str:
    nb=len(lst_val)
    code=""
    if center:
        code+="\\begin{center}\n"
    code+="\\begin{tabular}{c*{"+str(nb)+"}{|p{0.5cm}}}\n Valeurs "
    for val in lst_val:
        code=code  + " & " + str(val)
    code=code+ "\\\\ \\hline \n Effectifs "
    for eff in lst_eff:
        code=code  + " & " + str(eff)
    if frequence:
        code=code + "\\\\ \\hline \n Fréquences"
        for i in range(nb):
            code=code + " & "
        code=code + "\\\\[0.5cm]"
    code=code+"\n\\end{tabular}\n"
    if center:
        code+="\\end{center}\n"
    return(code)

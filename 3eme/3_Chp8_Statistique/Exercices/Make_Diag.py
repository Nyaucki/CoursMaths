
def diag_mk(lst_val,lst_eff,center=True,not_empty=True)->str:
    nb=len(lst_val)
    mx=max(lst_eff)
    code=""
    if center:
        code="\\begin{center} \n"
    code+="\\begin{tikzpicture}\n\\draw [<->] (0,"+str(  mx+0.5)+") node[above left]{Effectifs}|- ("+str(nb+0.5)+",0) node[below right]{Valeurs};\n"
    code+="\\foreach \\x in {0,...,"+str(mx)+"}\n{\n\\draw[lightgray,thin] (0,\\x)--("+ str(nb+0.5)+",\\x);\n}\n"
    if not_empty: # Même si pas élégant, double .replace marche Je suis preneur d'une solution plus élégante
        code+="\\foreach \\z [count=\\zi] in {"+str(lst_val).replace("[","").replace("]","") +"}{\n\\node at (\\zi - 0.5,-0.5) {\\z};\n}\n\\foreach \\x in {0,...,"+str(mx)+"}\n{\n\\draw (-0.1,\\x) node[left]{\\x} --(0.1,\\x);\n}\n\\foreach \\y [count=\\yi] in {"+str(lst_eff).replace("[","").replace("]","")+"}\n{\n\\draw[fill=white] (\\yi -1,0) rectangle (\\yi,\\y);\n}\n"
    code+="\\end{tikzpicture}\n"
    if center :
        code+="\\end{center}\n"
    return(code)



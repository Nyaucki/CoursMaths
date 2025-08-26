import os

def pyramide(path,name,triangle,scale=1.5):
    with open(path+"/"+name+".tex","w") as file:
        file.write("\\begin{center}\n\t\\begin{tikzpicture}[scale="+str(scale)+"]\n")
        for count,ligne in enumerate(triangle):
            file.write(" \t\t\\foreach \\j [count=\\xi]  in {"+str(ligne).replace("[","").replace("]","")+"}\n \t\t\t\t{\\draw ("+str(-3-count)+"+2*\\xi,"+str(-1*count)+") rectangle ("+str(-1-count)+"+2*\\xi,"+str(-1*count+1)+");\n \t\t\t\t\\node at ("+str(-2-count)+"+2*\\xi,"+str(-1*count+0.5)+") {\\j};}\n")
        file.write("\\end{tikzpicture}\n\t\\end{center}\n")

if __name__=="__main__":
    pyramide([[1],[2,3],[4,5,6]])

#!/usr/bin/env python3
import os
import sqlite3
from Correction_noteDS import *
from Correction_noteDM import *

conn = sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db')
reader_eleve=conn.cursor()

classe=input('Quelle est la classe ?')

devoir=input('Quelle est le numéro du devoir ?')

liste = reader_eleve.execute("SELECT nom,prenom FROM Eleve WHERE classe=?",(classe,))

code_a_remplacer = open("/home/nyaucki/Documents/Prof/CoursMaths/Database/corriger/corrigeA.tex").read()

entete_a_remplacer=open("/home/nyaucki/Documents/Prof/CoursMaths/Database/corriger/entete.tex").read()

with open("/home/nyaucki/Documents/Prof/CoursMaths/Database/corriger/docs_sensible/CorrigeEntier.tex","w") as fichier :
    fichier.write("\\documentclass{/home/nyaucki/Documents/Prof/CoursMaths/Database/corriger/activite}\n\\usepackage{tabularx}\n\\usepackage{pythontex}\n\\renewcommand{\\arraystretch}{1.5}\n\\begin{document}\n")
    for eleve in liste:
        comp=notes_competences(eleve,devoir)
        entete=entete_a_remplacer.replace('\\nom',eleve[0]+' ' +eleve[1])
        entete=entete.replace('\\classe',classe)
        entete=entete.replace('\\devnum',devoir)
        if comp['bareme_calculer']==0:
            entete=entete.replace('\\compeval{\\calculer}{calculer}','calculer\\\\non evalué')
        else :
            entete=entete.replace('\\calculer',str(comp['note_calculer']/comp['bareme_calculer']))
        if comp['bareme_raisonner']==0:
            entete=entete.replace('\\compeval{\\raisonner}{raisonner}','raisonner\\\\non evalué')
        else :
            entete=entete.replace('\\raisonner',str(comp['note_raisonner']/comp['bareme_raisonner']))
        if comp['bareme_modeliser']==0:
            entete=entete.replace('\\compeval{\\modeliser}{modéliser}','modéliser\\\\non evalué')
        else :
            entete=entete.replace('\\modeliser',str(comp['note_modeliser']/comp['bareme_modeliser']))
        if comp['bareme_chercher']==0:
            entete=entete.replace('\\compeval{\\chercher}{chercher}','chercher\\\\non evalué')
        else :
            entete=entete.replace('\\chercher',str(comp['note_chercher']/comp['bareme_chercher']))
        if comp['bareme_communiquer']==0:
            entete=entete.replace('\\compeval{\\communiquer}{communiquer}','communiquer\\\\non evalué')
        else :
            entete=entete.replace('\\communiquer',str(comp['note_communiquer']/comp['bareme_communiquer']))
        if comp['bareme_representer']==0:
            entete=entete.replace('\\compeval{\\representer}{représenter}','représenter\\\\non evalué')
        else :
            entete=entete.replace('\\representer',str(comp['note_representer']/comp['bareme_representer']))
        code=code_a_remplacer
        entete=entete.replace('\\note',str(note((devoir,eleve[0],eleve[1]))))
        # code.replace('\\bareme1',str())
        fichier.write(entete)
        # fichier.write(code)
        # fichier.write('\n')
        # fichier.write('\\newpage\n')
    fichier.write('\\end{document}')

# for i in range(len(noms)):
#         code = code_a_remplacer.replace('\\nom',noms[i] + ' ' + prenoms[i])
#         code = code.replace('\\prenom',prenoms[i])
#         fichier.write(code)
#         fichier.write('\n')
#         fichier.write('\\newpage\n')

os.system('make')

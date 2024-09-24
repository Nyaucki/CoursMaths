import csv
import sqlite3
from datetime import datetime

connection = sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db')
cursor = connection.execute('select * from Reponses')
names = list(map(lambda x: x[0], cursor.description))#obtenir le nom des colones de la table Reponses
names=[names]#Doit être mis sous forme de liste pour être lu correctement

cls=input('Quelle est la classe concernée ?')
classe=(cls,)

cur = connection.cursor()
res_eleves = cur.execute("SELECT nom,prenom,classe FROM Eleve WHERE classe = ? ORDER BY nom",classe)#Obtenir la liste des élèves d'une classe

annee = datetime.now().year
if datetime.now().month <8:
    annee+=1
annee_str=str(annee) +'/'+ str(annee+1)#pour année scolaire

with open('/home/nyaucki/Documents/Prof/CoursMaths/Database/ressources/Liste_Reponses.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(names)
    with open('/home/nyaucki/Documents/Prof/CoursMaths/Database/ressources/Liste_Questions_pure.csv',"r") as questions:
        next(questions)#saute les header
        reader_questions = csv.reader(questions)
        for row_elv in res_eleves:
            for row_qu in reader_questions:
                if row_qu[13]=="FALSE":
                    row=[]
                    row.append(row_qu[0])#Devoir
                    row.append(row_qu[1])#Exercice
                    row.append(row_qu[2])#Question
                    row.append(row_qu[3])#Niveau
                    row.append(row_elv[0])#Nom
                    row.append(row_elv[1])#Prenom
                    row.append(row_elv[2])#Classe
                    row.append(annee_str)#annee scolaire
                    writer.writerows([row])
            questions.seek(0) #revient au début du fichier
            next(questions)#saute les header
import sqlite3
from datetime import datetime
import csv

with open("/home/nyaucki/Documents/Prof/CoursMaths/Database/ressources/Liste_Questions.csv", newline='') as in_file:
    with open("/home/nyaucki/Documents/Prof/CoursMaths/Database/ressources/Liste_Questions_pure.csv", 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(row):
                writer.writerow(row)

in_file.close()

def add_question(conn, question):
    sql = ''' INSERT INTO Questions(devoir,exercice,question,niveau,chapitre,tag,competence,modalite,bareme,erreur_calcul,erreur_cours,erreur_preuve,erreur_innatention,hors_bareme,annee)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, question)
    conn.commit()
    return cur.lastrowid

liste = open("/home/nyaucki/Documents/Prof/CoursMaths/Database/ressources/Liste_Questions_pure.csv","r")
next(liste)#saute les headder
listeQuestions = liste.read()
listeQuestions = listeQuestions.split('\n')
listeQuestions.remove('')

annee = datetime.now().year
if datetime.now().month >7:
    annee+=1
annee_str=str(annee) +'/'+ str(annee+1)#pour année scolaire

# liste.close()

def main():
    try:
        with sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db') as conn:
            for i in range(len(listeQuestions)):
                question=()
                nuplet=listeQuestions[i].split(',')#change data de string à nuplet
                for j in nuplet:
                    question+=(j,) #formulation spécifique au tuple
                question+=(annee_str,)
                add_question(conn, question)

    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    main()

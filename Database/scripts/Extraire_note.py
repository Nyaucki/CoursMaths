import csv
import sqlite3

conn = sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db')
cursor = conn.cursor()

def extract_notes(classe,devoir):
    col_devoir='Devoir_'+devoir
    notes=cursor.execute('''SELECT nom , prenom , (%s) FROM Eleve  WHERE classe = (?) '''%(col_devoir), (classe,))
    with open('/home/nyaucki/Documents/Prof/CoursMaths/Database/ressources/Liste_Notes.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for eleves in notes :
            row=[]
            row.append(eleves[0])#nom
            row.append(eleves[1])#prenom
            row.append(eleves[2])#note
            writer.writerows([row])#ajoute au csv
if __name__ == '__main__':
    classe = input("Quelle est la classe :")
    devoir = input("Quelle est le numero du devoir :")
    extract_notes(classe,devoir)

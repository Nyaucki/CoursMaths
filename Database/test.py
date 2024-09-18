import sqlite3
from datetime import datetime
import csv

julie=('4eme3','COSSARD')

connection = sqlite3.connect('my.db')
cur = connection.cursor()
# res_eleves = cur.execute("SELECT nom,prenom,classe FROM Eleve WHERE classe = ? ORDER BY nom",classe)#Obtenir la liste des élèves d'une classe

res_eleves = cur.execute("SELECT nom,prenom,classe FROM Eleve WHERE classe = ?AND nom= ? ORDER BY nom",julie)#Obtenir la liste des élèves d'une classe

def bareme(conn,question):
    cur = conn.cursor()
    bareme=cur.execute("SELECT bareme,erreur_calcul,erreur_cours,erreur_preuve,erreur_innatention FROM Questions WHERE devoir = ? AND exercice = ? AND question = ? and niveau= ?",question)
    for item in bareme: 
        return(item)

if __name__ == '__main__':
    # with sqlite3.connect('my.db') as conn:
    #     a=bareme(conn,(1,'',2,3))
    #     print(a)
    # b=('',2)
    # print(int(b[0])+b[1])
    note=-1
    note=max(0,note)
    print(note)

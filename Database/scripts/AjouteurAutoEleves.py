import sqlite3
from datetime import datetime

def add_eleve(conn, eleve):
    sql = ''' INSERT INTO Eleve(prenom,nom,classe,annee)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, eleve)
    conn.commit()
    return cur.lastrowid

liste = open("/home/nyaucki/Documents/Prof/CoursMaths/Database/ressources/Liste_Eleves.csv","r")
listeNoms = liste.read()
listeNoms = listeNoms.split('\n')
# listeNoms.remove('')

noms,prenoms=[],[]
for paire in listeNoms:
    y = paire.split(',')
    #y.remove('')
    noms.append(y[0])
    prenoms.append(y[1])

    
liste.close()

def main(classe):
    try:
        with sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db') as conn:
            for i in range(len(noms)):
                eleve = (prenoms[i], noms[i], classe, datetime.now().year)
                add_eleve(conn, eleve)
        conn.commit()#commit the change


    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    classe = input("Quelle est la classe :")
    main(classe)
    

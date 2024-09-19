import sqlite3

conn = sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db')
cursor = conn.cursor()
cur=conn.cursor()
cursor_note=conn.cursor()

def add_column(Devoir_nb):#Ajoute une colone si n'existe pas
    table='Eleve'
    new_column='Devoir_'+Devoir_nb
    cursor.execute('PRAGMA table_info({})'.format(table))
    columns = [row[1] for row in cursor.fetchall()]
    if new_column not in columns:
        cursor.execute('ALTER TABLE {} ADD COLUMN {} INTEGER'.format(table,new_column))

def note(devoir_eleve): #recupère les notes du DM
    notes=cursor_note.execute("SELECT note FROM Reponses WHERE devoir = ? AND nom = ? AND prenom = ?",devoir_eleve)
    return sum(item[0] for item in notes)

def add_notes(classe,devoir):
    col_devoir='Devoir_'+devoir
    eleves=cursor.execute("SELECT nom,prenom FROM Eleve WHERE  classe= ?",(classe,))
    # eleves=cursor.fetchall()
    for item in eleves :
        recherche=(devoir,)
        recherche+=item
        note_eleve=(note(recherche),)
        note_eleve+=item
        note_eleve+=(classe,)
        cur.execute('''UPDATE Eleve set (%s) = (?) WHERE nom = (?) AND prenom = (?) and classe = (?) '''%(col_devoir), note_eleve)#different cursor name to avoid confusion




if __name__ == '__main__':
    classe = input("Quelle est la classe :")
    devoir = input("Quelle est le numero du devoir :")
    add_column(devoir)
    add_notes(classe,devoir)
    
    #Commit the change
    conn.commit()
    conn.close()
import sqlite3
import csv
from Extraire_note import *

conn = sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db')
writer_column = conn.cursor()
reader_reponse=conn.cursor()
reader_bareme=conn.cursor()
reader_competence1=conn.cursor()
reader_competence2=conn.cursor()


def add_column(Devoir_nb):#Ajoute une colone si n'existe pas
    table='Eleve'
    new_column='Devoir_'+Devoir_nb
    writer_column.execute('PRAGMA table_info({})'.format(table))
    columns = [row[1] for row in writer_column.fetchall()]
    if new_column not in columns:
        writer_column.execute('ALTER TABLE {} ADD COLUMN {} INTEGER'.format(table,new_column))

def note_exo(devoir_eleve,num_exo): #recupère les notes du DM
    exo_eleve=devoir_eleve
    exo_eleve+=(num_exo,)
    notes=reader_reponse.execute("SELECT note FROM Reponses WHERE devoir = ? AND nom = ? AND prenom = ? AND exercice = ?",exo_eleve)
    return sum(item[0] for item in notes)

def bareme_exo(num_devoir,num_exo,niveau):
    bareme=reader_bareme.execute("SELECT bareme FROM Questions WHERE devoir = ? AND exercice = ? AND niveau=? AND hors_bareme='FALSE' ",(num_devoir,num_exo,niveau))
    return int(sum(item[0] for item in bareme))

def notes_competences(eleve,num_devoir):
    calculer_note,calculer_bareme=0,0
    chercher_note,chercher_bareme=0,0
    raisonner_note,raisonner_bareme=0,0
    communiquer_note,communiquer_bareme=0,0
    representer_note,representer_bareme=0,0
    modeliser_note,modeliser_bareme=0,0
    devoir_eleve=(num_devoir,)
    devoir_eleve+=eleve
    reponses=reader_competence1.execute("SELECT exercice,question,note FROM Reponses WHERE devoir = ? AND nom = ? AND prenom = ? AND non_fait = 0",devoir_eleve)
    for row in reponses:
        reader_competence2.execute("SELECT bareme,competence FROM Questions WHERE devoir = ? AND exercice = ? AND question = ? ",(num_devoir,row[0],row[1]))
        search_comp=reader_competence2.fetchone()
        if search_comp[1]=="calculer":
            calculer_note+=row[2]
            calculer_bareme+=search_comp[0]
        elif search_comp[1]=="chercher":
            chercher_note+=row[2]
            chercher_bareme+=search_comp[0]
        elif search_comp[1]=="raisonner":
            raisonner_note+=row[2]
            raisonner_bareme+=search_comp[0]
        elif search_comp[1]=="modéliser":
            modeliser_note+=row[2]
            modeliser_bareme+=search_comp[0]
        elif search_comp[1]=="communiquer":
            communiquer_note+=row[2]
            communiquer_bareme+=search_comp[0]
        elif search_comp[1]=="représenter":
            representer_note+=row[2]
            representer_bareme+=search_comp[0]
    return dict(note_calculer=calculer_note,bareme_calculer=calculer_bareme,note_chercher=chercher_note,bareme_chercher=chercher_bareme,note_communiquer=communiquer_note,bareme_communiquer=communiquer_bareme,note_raisonner=raisonner_note,bareme_raisonner=raisonner_bareme,note_representer=representer_note,bareme_representer=representer_bareme,note_modeliser=modeliser_note,bareme_modeliser=modeliser_bareme)









if __name__ == '__main__':
    classe = input("Quelle est la classe :")
    devoir = input("Quelle est le numero du devoir :")
    add_column(devoir)
    conn.commit()#commit the change
    extract_notes(classe,devoir)

    conn.close()
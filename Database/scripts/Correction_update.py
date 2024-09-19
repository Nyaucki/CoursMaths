import sqlite3
from datetime import datetime
import csv

#A faire  

def add_reponse(conn, reponse):#fonction qui ajoute des réponses
    sql = ''' INSERT OR IGNORE INTO Reponses(devoir,exercice,question,niveau,nom,prenom,classe,annee,non_fait,hors_sujet,innatention,cours_non_su,fraction,pas_une_preuve,signes,priorite,calcul,pas_de_detail,note)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, reponse)
    conn.commit()
    return cur.lastrowid

liste = open("/home/nyaucki/Documents/Prof/CoursMaths/Database/ressources/Liste_Reponses.csv","r")
next(liste)#saute les headder
listeReponses = liste.read()
listeReponses = listeReponses.split('\n')
listeReponses.remove('')

def bareme(conn,question): #renvoie le bareme et les points par erreur
    cur = conn.cursor()
    bareme=cur.execute("SELECT bareme,erreur_calcul,erreur_cours,erreur_preuve,erreur_innatention FROM Questions WHERE devoir = ? AND exercice = ? AND question = ? and niveau= ?",question)
    for item in bareme: 
        return(item)


def main():
    try:
        with sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db') as conn:
            for i in range(len(listeReponses)):#pour chaque ligne de l'excel
                reponses=()
                nuplet=listeReponses[i].split(',') #change data de string à nuplet
                for idx, item in enumerate(nuplet):
                    if idx != 18: #pour retirer la colonne Note du csv. Si ne marche pas, on peut juste mettre enumerate(nuplet[:-1])
                        if item=='' and idx>7:
                            reponses+=(0,) #remplace les empty string par des 0
                        else :
                            item_int=item
                            try : #Pour ne pas modifier ce qui ne peut pas l'être
                                item_int=int(item)
                            except ValueError as verr:
                                pass
                            reponses+=(item_int,) #formulation spécifique au tuple
                bar=bareme(conn,(reponses[0],reponses[1],reponses[2],reponses[3]))
                note=bar[0] #bareme de la question
                note=note-bar[1]*(reponses[12]+reponses[14]+reponses[15]+reponses[16]) #erreur de calcul
                note=note-bar[2]*(reponses[11]) #erreur de cours
                note=note-bar[3]*(reponses[13]+reponses[17]) #erreur de preuve
                note=note-bar[4]*(reponses[10]) #erreur d'inattention
                if reponses[8]+reponses[9]>0 : #si non fait ou hors sujet
                    note=0
                note=max(0,note) #pour ne pas avoir de notes négatives
                reponses+=(note,) #on ajoute la note
                add_reponse(conn,reponses)

    except sqlite3.Error as e:
        print(e)



if __name__ == '__main__':
    main()

import sqlite3
import csv

conn = sqlite3.connect('/home/nyaucki/Documents/Prof/CoursMaths/Database/my.db')
cursor = conn.cursor()

def add_column(classe,Devoir_nb):
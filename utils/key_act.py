import sqlite3
from database.connect import cr_table
from tabulate import tabulate

conn=sqlite3.connect("database/keywords.db")
cursor=conn.cursor()

def add_key(keywd):
    cr_table()
    cursor.execute('''INSERT INTO keywords (keyword)
              VALUES(?)
                   ''',(keywd,))
    conn.commit()

def del_key(keywd):
    cursor.execute('''DELETE FROM keywords WHERE id=(?)''',(keywd,))
    conn.commit()

def get_key():
    cursor.execute('''SELECT keyword FROM keywords''')
    rows=cursor.fetchall()
    return [row[0] for row in rows]


def show_key():
    cursor.execute("SELECT * FROM keywords")
    rows = cursor.fetchall()

    print(tabulate(rows, headers=["ID", "Keyword", "Date"], tablefmt="grid"))
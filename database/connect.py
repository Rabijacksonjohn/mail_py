import sqlite3
from tabulate import tabulate


conn=sqlite3.connect("database/keywords.db")
cursor=conn.cursor()

def cr_table():
    cmd='''CREATE TABLE IF NOT EXISTS keywords(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT UNIQUE NOT NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP ) '''
    cursor.execute(cmd)
    conn.commit()
    print("database is created")

def del_table():
    cmd='''DROP TABLE IF EXISTS keyword_tab'''
    cursor.execute(cmd)
    conn.commit()
    print("database is deleted")

def show_table():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(tabulate(tables, headers=["Table Name"], tablefmt="grid"))


# try :
#     cr_table()
#     show_table()
#     del_table()
#     show_table()
# except Exception as e:
#     print(e)
import sqlite3


# Create a database
connection=sqlite3.connect('keyword_company.db')

cursor=connection.cursor()

command1 = '''CREATE TABLE IF NOT EXISTS keyword (
    email_id TEXT PRIMARY KEY, 
    keyword_matched TEXT,
    date_found DATETIME DEFAULT CURRENT_TIMESTAMP
)'''

cursor.execute(command1)
connection.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables=cursor.fetchall()

print("Tables in the database")
for i in tables:
    print(i)
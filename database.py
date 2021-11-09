import sqlite3
con = sqlite3.connect('baza.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS user
               (ID INTEGER PRIMARY KEY , name text, email text, password text, kontakt text, created_a text)''')

con.commit()

con.close()

import sqlite3
con = sqlite3.connect('baza.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
               ( id INTEGER PRIMARY KEY  , name text, email text, password text, kontakt text,  created_at text, br_prijava INTEGER DEFAULT 0)''')


con.commit()


con.close()



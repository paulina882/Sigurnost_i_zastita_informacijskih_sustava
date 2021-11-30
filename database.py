import sqlite3
con = sqlite3.connect('baza.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
               ( id INTEGER PRIMARY KEY  , name text, email text, password text, kontakt text,  created_at text, br_prijava INTEGER DEFAULT 0)''')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS forgot_password
               ( user_id INTEGER PRIMARY KEY, hash text, valid_until text)''')


con.commit()


con.close()



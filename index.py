import sqlite3
from datetime import date
print('Dobrodošli u Unidu sustav')
print('Za prijavu unesite broj 1, za registraciju broj 2:')
broj=0
dopusteni=[1,2]
def register_user():
        con=con = sqlite3.connect('baza.db')
        cur = con.cursor()
        ime=input('Unesite ime:')
        email=input('Unesite email:')
        password=input('Unesite password:')
        kontakt=input('Unesite kontakt:')
        created_at=date.today()
        cur.execute("INSERT INTO user(name, email, password, kontakt, created_a) VALUES (?, ?, ?, ?, ?)",(ime, email, password, kontakt, created_at))
        con.commit()
        con.close()
        
        return print('Uspiješno ste unjeli korisnika!')
while broj not in dopusteni:
    broj=int(input('Unesite broj:'))
if broj==1:
    print("Dobrodošli u Prijavu!")
if broj==2:
    print("Dobrodošli u registraciju!")
    register_user()
    




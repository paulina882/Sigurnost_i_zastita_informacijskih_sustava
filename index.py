import sqlite3
from datetime import date
print('Dobrodošli u Unidu sustav')
print('Za prijavu unesite broj 1, za registraciju broj 2:')
broj=0
dopusteni=[1,2]
brojac=0

def login():
        email = input("Unesi email: ")
        password = input("Unesi lozinku: ")
        
        con=con = sqlite3.connect('baza.db')
        cur = con.cursor()
        korisnik=cur.execute("SELECT password,br_prijava,name FROM users WHERE email = ?", (email))
        korisnik=cur.fetchone();
        brojac = int(korisnik[1])
        ime = korisnik[2]
                        
        if(korisnik[0]==password):
                print("Dobrodosao ")
                print(ime)
                print("Korisnik postoji i broj prijava je : ")
                brojac=brojac +1
                print(brojac)
                brojac=str(brojac)
                cur.execute("update users SET br_prijava = ? where email = ?", (brojac ,email))
                con.commit()
                con.close()
        
def register_user():
        con=con = sqlite3.connect('baza.db')
        cur = con.cursor()
        ime=input('Unesite ime:')
        email=input('Unesite email:')
        password=input('Unesite password:')
        kontakt=input('Unesite kontakt:')
        created_at=date.today()
        cur.execute("INSERT INTO users(name, email, password, kontakt, created_at, br_prijava) VALUES (?, ?, ?, ?, ?, ?)",(ime, email, password, kontakt, created_at, 0))
        con.commit()
        con.close()
        
        return print('Uspiješno ste unjeli korisnika!')
while broj not in dopusteni:
    broj=int(input('Unesite broj:'))
if broj==1:
    print("Dobrodošli u Prijavu!")
    login()
if broj==2:
    print("Dobrodošli u registraciju!")
    register_user()
    




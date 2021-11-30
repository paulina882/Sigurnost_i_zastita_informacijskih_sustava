import sqlite3
import time
from datetime import date


print('Dobrodošli u Unidu sustav')
print('Za prijavu unesite broj 1, za registraciju broj 2, za zaboravljenu lozinku 3:')
broj=0
dopusteni=[1,2, 3]
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
def forgot():
        email=input('Unesite email:')
        con=con = sqlite3.connect('baza.db')
        cur = con.cursor()
        korisnik=cur.execute("SELECT email FROM users WHERE email = ?", (email))
        korisnik=cur.fetchone();
        if (korisnik==None):
                
                print("Uneseni email se ne nalazi u bazi!")
                return
        else:
                hashv=hash(time.time())
                print(hashv)
                
                cur.execute("INSERT INTO forgot_password(user_id, hash, valid_until) VALUES (?, ?, ?)",(hashv, ))
        

        
        
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
if broj==3:
        print("Dobrodošli u promjenu lozinke!")
        forgot()
    




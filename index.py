print('Dobrodošli u Unidu sustav')
print('Za prijavu unesite broj 1, za registraciju broj 2:')
broj=0
dopusteni=[1,2]
while broj not in dopusteni:
    broj=int(input('Unesite broj:'))
if broj==1:
    print("Dobrodošli u Prijavu!")
if broj==2:
    print("Dobrodošli u registraciju!")

  

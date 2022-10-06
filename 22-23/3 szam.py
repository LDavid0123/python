import random

a = int(input('Adj meg egy konstans számot! '))
b = random.randint(5,25)
c = int(input('Adj meg egy tetszőleges számot! '))
osszeg = a+b+c
osszeg2 = a*b*c
print (osszeg)
print (osszeg2)
if osszeg2 > 500:
    print('a szorzat nagyobbb mint 500')
else:
    print('Nem nagyobb mint 500')
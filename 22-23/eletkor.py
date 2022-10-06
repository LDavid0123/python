
nev = input("Kérem adja meg a nevét ")
print(nev)
ÉV =2022
udv = (f'Üdvözöllek {nev}')
print(udv,"szép napot kívánok neked", sep = " ")
eletkor = int(input("Kérem adja meg a születési évét "))
eletk = ÉV- eletkor

if eletk < 14:
    print('Általános iskolás vagy!')
elif eletk > 14 | eletk < 18:
    print('Középiskolás vagy!')
elif eletk > 18:
    print('Felnőtt vagy!')

# név
# automarka
# gyárto, orszag, vegsebesség

nev = input("Kérem adja meg a nevét ")
automarka = input("Kérem adja meg az autó márkáját ")
vegsebesseg = int(input("Mennyivel megy ez a " +automarka+ '? '))
orszag = input("Hol készül a " +automarka+ '? ')
mondat1 = orszag + ' vidékein készül a ' + automarka + ', ami ' + str(vegsebesseg) + ' km/h-val megy'
print(mondat1)

mondat2 = '{} vidékein készül a {}, ami {} km/h-val megy' .format(orszag, automarka, vegsebesseg)
print(mondat2)

mondat3 = '{0} vidékein készül a {1}, ami {2} km/h-val megy' .format(orszag, automarka, vegsebesseg)
print(mondat3)

mondat4 = '{o} vidékein készül a {a}, ami {v} km/h-val megy' .format(o=orszag, a=automarka, v=vegsebesseg)
print(mondat4)

NÉMET = 19
BRIT = 20
CSEH = 21
LENGYEL = 23
MAGYAR = 27

nettó_ár = float(input('Hogyér/' 'adnak egy mütyürkét? '))
print(f'A mütyürke bruttó árai: ')

print(f'{nettó_ár*(1+NÉMET/100):10.2f} picula társaságában')

print(f'{nettó_ár*(1+BRIT/100):^10.2f} picula társaságában')
print(f'{nettó_ár*(1+CSEH/100):10.2f} picula társaságában')
print(f'{nettó_ár*(1+LENGYEL/100):10.2f} picula társaságában')
print(f'{nettó_ár*(1+MAGYAR/100):10.2f} picula társaságában')

hofok = int(input('Kérem adja meg a hőfokot! '))
olvadas = 1539
forras = 2750
if hofok < olvadas:
    print("Szilárd")
elif hofok < forras:
    print("Folyékony")
else:
    print("Gáz")
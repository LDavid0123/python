from __future__ import print_function
from itertools import count


szorzando = 5
szorzo = input('Mennyivel szorozzam meg az ' + str(szorzando) +'-öt? ')
print(szorzando, '-ször ', szorzo, ' annyi mint ', sep='', end='')
szorzo = int(szorzo)
print(szorzando*szorzo)


ellenseg = input('Ki volt a Piroska nevű szuperhős főellensége? ')
if ellenseg == 'farkas' or ellenseg == 'Farkas':
    print('Okos vagy.')
    print('Nem is kicsit.')
elif ellenseg == 'ordas':
    pass
else:
    print('Hááááát...')
    print('Nem.')
print('Legközelebb a hét törpét kérdezem visszafelé!')


osszeg = None
while osszeg != 4:
    osszeg = input('Mennyi kétszer kettő? ')
    osszeg = int(osszeg)
print('Annyi.')


varosok = ['Miskolc', 'Párizs', 'Dublin', 'Lajosmizse']

for varos in varosok:
    print(varos, 'egy város Európában')

for index, varos in enumerate(varosok):
    print(varos, 'egy város Európában')
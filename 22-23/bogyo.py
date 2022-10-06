név = input('Mi az ős neve? ')
bogyók = int(input('Hány bogyója van? '))

if bogyók < 10:
    minősítés = 'zsenge'
elif bogyók > 20:
    minősítés = 'nagy koponya'
else:
    minősítés = 'gyűjtögető'

print(f'{név} egy {minősítés}.')

barack = int(input('Hány mázsa barack termett? '))
ar = int(input('Mennyibe kerül 1 darab? '))
korte = int(input('Hány mázsa körte termett? '))
ar2 =int(input('Mennyibe kerül 1 darab? '))

if barack>korte:
    print('Barackból több van')
elif korte>barack:
    print('Körtéből több van')
else:
    print('Egyenlő')
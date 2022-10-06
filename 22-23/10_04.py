össz = 0
ivás = 0

while össz <= 35 and (ivas:=int(input('Hány decit ittál? '))):
    print(f'Már{(össz:=össz+ivás)/10:3.1f}litert ittál. ')
    if össz >= 25:
        print('Már sikerült elérdned a 2,5 litert.')
print('Béka nő a hasadba')
nev = input('Mi a gép neve? ')
mukodik = True if input('Működik? i/n') == 'i' else False
ar = int(input('Mi az ára? '))

if (nev == 'ZX Spectrum' or nev == 'C64') and mukodik and ar <= 25000:
    print('Biznisz! ')
else:
    print('Gagyi 8 bitesek... Kinek kellenek?')
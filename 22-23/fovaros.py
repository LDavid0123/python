
import random

fovarosok = []
fovarosok = ["Bécs", "Bern", "Párizs", "London", "Budapest", "Varsó", "Prága", "Róma", "Madrid", "Helsinki", "Moszkva"]
fvaros = None
while fvaros !='':
    print('fővarosok jelenleg:', ', '.join(fovarosok))
    fvaros = input('Kérek egy fővárost!')
    if fvaros !='':
        fovarosok.append(fvaros)
#n = random.randint(1,len(fovarosok)-1)

for index, fovaros in enumerate(fovarosok):
    print(index, fovarosok)

#n = int(subset)
#print('A számítógép szerint ez a főváros a legszebb:', fovarosok[n])

while len(fovarosok)>0:
    print('Fővárosaink:', ', '.join(fovarosok))
    melyik = input('Melyik főváros a legszebb, válaszd ki! ')
    if melyik in fovarosok:
        fovarosok.remove(melyik)
    else:
        print('Ilyen főváros nincs a listába')
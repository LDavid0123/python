ft = int(input('Hány forintot költöttél szerdán? '))
ft2 = int(input('Hány forintot költöttél csütörtökön? '))

if ft>ft2:
    print('Szerdán költöttél többet,', ft)
elif ft2>ft:
    print('Csütörtökön költöttél többet,', ft2)

for i in range (1,101):
    print(i)

for i in range (100):
    print(i)

for i in range (1,101,2):
    print(i)

for i in range (100,1):
    print(i)

for i in range (100,1,-2):
    print(i)

szoveg = "alma:körte:barack"
elso, masodik, harmadik = szoveg.split(':')

ip=input("IP cím: ")
ipDigitsStr=ip.replace('.', '')
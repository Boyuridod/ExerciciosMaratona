# https://vjudge.net/contest/743937#problem/B

def tostring(x):
    x = str(x)

    if(len(x) == 1):
        return "0" + x
    
    return x

def testaPalindromo(hora, minuto):
    hora = tostring(hora)
    minuto = tostring(minuto)

    hora = hora[1] + hora[0]

    return (hora == minuto)

hh, mm = input().split(":")
hh = int(hh)
mm = int(mm)

mm += 1

if(mm == 60):
    mm = 00
    hh += 1

if(hh == 24):
    hh = 0

while(not testaPalindromo(hh, mm)):
    mm += 1

    if(mm == 60):
        mm = 00
        hh += 1

    if(hh == 24):
        hh = 0

print(f"{tostring(hh)}:{tostring(mm)}")
# https://vjudge.net/problem/UVA-11786

import re

def exercicio():
    relevo = list(input())

    cont = 0

    for i in range(len(relevo) - 1, 0, -1):
        if(relevo[i] == "/"):
            cont = i
            break

    relevo = relevo[0: cont]

    while(True):
        try:
            relevo.pop(relevo.index("/"))
        except:
            break

    area = 0
    cont = 0
    i = 0
    lenrelevo = len(relevo)
    
    while(i < lenrelevo):
        if(relevo[i] == '\\'):
            cont += 1

        else:
            area += cont
            relevo.pop(i)
            lenrelevo -= 1

        i += 1

    area += len(relevo)

    print(area)

T = int(input())

while(T > 0):
    exercicio()

    T -= 1
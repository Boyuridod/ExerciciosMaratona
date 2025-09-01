# https://vjudge.net/contest/744581#problem/E

N = int(input())

palavra = input()

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def testa(pala):
    for i in alfabeto:
        if(i not in pala and i.upper() not in pala):
            return "NO"
        
    return "YES"

if(len(palavra) < 26):
    print("NO")

else:
    print(testa(palavra))
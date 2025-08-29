# https://vjudge.net/contest/743937#problem/A

vogais = ["a", "e", "i", "o", "u"]

palavra = input()

def testa(palavra):
    for i in range(len(palavra) - 1):
        if(palavra[i] not in vogais):
            if(palavra[i + 1] not in vogais and palavra[i] != "n"):
                return "NO"
            
    if(palavra[-1] not in vogais and palavra[-1] != "n"):
        return "NO"

    return "YES"

print(testa(palavra))
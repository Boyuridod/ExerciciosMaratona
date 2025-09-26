# https://open.kattis.com/problems/lvable

N = int(input())
palavra = input()

def exercicio(palavra):
    for i in range(N - 1):
        if(palavra[i] == "l" and palavra[i + 1] == "v"):
            return 0
    
    if("l" in palavra):
        return 1
        
    elif("v" in palavra):
        return 1
        
    else:
        return 2
        
print(exercicio(palavra))
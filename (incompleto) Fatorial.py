# https://neps.academy/br/exercise/1329

N = int(input())

fat = [1, 1]

i = 2

cont = 0

while(i < 9):
    fat.append(fat[i - 1] * i)

    i += 1

i = 8

while(i > 0):
    
    if(N > fat[i]):
        N -= fat[i]

        cont += 1

        i += 1

    i -= 1

print(cont)
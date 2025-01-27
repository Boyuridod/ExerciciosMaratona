risada = list(input())

vogais = ["a", "e", "i", "o", "u"]

vog_ris = []

certo = True

for i in risada:
    if(i in vogais):
        vog_ris.append(i)

i = 0
j = len(vog_ris) - 1

while(i < j and certo == True):
    if(vog_ris[i] == vog_ris[j]):
        i += 1
        j -= 1
    else:
        certo = False

if(certo == True):
    print("S")

else:
    print("N")
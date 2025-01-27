palavra = input()

vogais = ["a","e","i","o","u","A", "E", "I", "O", "U"]

cont = 0

for i in palavra:
    if(i in vogais):
        cont += 1

print(cont)
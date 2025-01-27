import math

frase = input()

vogais = ['A', 'E', 'I', 'O', 'U']

v = []
c = []

for i in frase:
    if(i in vogais):
        v.append(i)
    elif(i != ' '):
        c.append(i)

r = 1
x = len(v)
y = len(c)

while(True):

    if(x > 0 and y >= 0):
        r *= x

    if(y > 0 and x >= 0):
        r *= y

    x -= 1
    y -= 1

    if(x <= 0 and y <= 0):
        break

print(r // 2)
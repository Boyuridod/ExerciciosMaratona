A1 = int(input())
A2 = int(input())
A3 = int(input())

tempo = 0

tempo = (A2 * 2) + (A3 * 4)

if(tempo > (A1 * 2) + (A3 * 2)):
    tempo = (A1 * 2) + (A3 * 2)

if(tempo > (A2 * 2) + (A1 * 4)):
    tempo = (A2 * 2) + (A1 * 4)

print(tempo)
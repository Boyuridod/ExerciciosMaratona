num = int(input())

v = []

v = (input().split(" "))

j = 0
a = 0
ido = 0

for i in range(len(v)):
    if(v[i] == '1'):
        a += 1
    elif(v[i] == '2'):
        j += 1
        ido += 1

print("Jovem:", j)
print("Adulta:", a)
print("Idosa:", ido)
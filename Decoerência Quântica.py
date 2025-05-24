N = int(input())
str1 = input()
str2 = input()

astPrimera = 0
astSegunda = 0

for i in range(N):
    if str1[i] == '*':
        astPrimera += 1
    if str2[i] == '*':
        astSegunda += 1

print(f'{(astPrimera - astSegunda) / astPrimera:.2f}')
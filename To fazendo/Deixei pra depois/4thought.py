# https://open.kattis.com/problems/4thought

ops = {}

T = int(input())

def exercicio():
    num = 4
    fin = int(input())
    out = ""

    for i in range(3):
        if(fin - num >= 4 * 4):
            out += "* 4 "
            num *= 4 * 4
        elif(fin - num >= 4 + 4):
            out += "+ 4 "
            num += 4 + 4
        elif(fin - num <= 4 / 4):
            out += "/ 4 "
            num /= 4
        elif(fin - num <= 4 - 4):
            out += "- 4 "
            num -= 4

        out += "+"

    if(num == 0):
        print(f"{out} = {num}")

    else:
        print("no solution")

for t in range(T):
    exercicio()
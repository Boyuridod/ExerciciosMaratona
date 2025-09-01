#https://vjudge.net/contest/743937#problem/D

def exercicio():
    monstros = list(map(int, input().split(" ")))

    total = 0

    while(total > 0):
        print(total)
        total += 6

        if(sum(monstros) - total < 3):
            return False
        else:
            for i in range(len(monstros)):
                monstros[i] -= 1

                if(monstros[i] == 0):
                    zeros += 1

            if(zeros % 3 != 0):
                return False
            
            if(zeros == 3):
                return True

t = int(input())

for i in range(t):
    if(exercicio()):
        print("YES")
    else:
        print("NO")
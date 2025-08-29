#https://vjudge.net/contest/743937#problem/D

def exercicio():
    monstros = list(map(int, input().split(" ")))

    round = 1

    total = sum(monstros)

    while(total > 0):

        if(round % 7 == 0):
            zeros = 0

            for i in range(len(monstros)):
                monstros[i] -= 1

                if(monstros[i] == 0):
                    zeros += 1

            if(zeros % 3 != 0):
                return False

        else:
            ataca = monstros.index(max(monstros))
            monstros[ataca] -= 1
            if(monstros[ataca] == 0):
                return False

        total = sum(monstros)

        if(round % 7 == 0 and total == 0):
            return True
        
        # print(monstros)

        round += 1

    return False


t = int(input())

for i in range(t):
    if(exercicio()):
        print("YES")
    else:
        print("NO")
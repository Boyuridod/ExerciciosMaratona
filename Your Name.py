# https://codeforces.com/contest/2167/problem/B

def exercicio():
    lenth = int(input())

    s, t = input().split(" ")

    stot = {}
    ttot = {}

    for i in range(lenth):
        try:
            stot[s[i]] += 1
        except:
            stot[s[i]] = 1

        try:
            ttot[t[i]] += 1
        except:
            ttot[t[i]] = 1

    for i in stot:
        if(stot.get(i) != ttot.get(i)):
            return ("NO")
        
    return("YES")
    

t = int(input())

for k in range(t):
    print(exercicio())
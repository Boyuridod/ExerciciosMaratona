# https://vjudge.net/problem/Kattis-pokerhand

cartas = input().split(" ")

poder = {}

for i in cartas:
    try:
        poder[i[0]] += 1
    except:
        poder[i[0]] = 1

print(max(poder.values()))
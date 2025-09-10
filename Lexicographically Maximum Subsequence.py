# https://vjudge.net/contest/746740#problem/J

st = list(input())

sete = list(set(st))
sete.sort(reverse=True)

for i in range(len(sete)):
    for j in range(len(st)):
        if(sete[i] == st[j]):
            print(sete[i], end="")
            last = j

    try:
        for j in range(last):
            st.pop(0)
    except:
        break

print("")
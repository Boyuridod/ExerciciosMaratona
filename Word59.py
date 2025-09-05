# https://codeforces.com/problemset/problem/59/A

palavra = input()

qttUper = 0
qttLower = 0

# print(ord("a"), ord("A"))

for i in palavra:
    # print(ord(i), ord("z"))
    if(ord(i) < ord("a")):
        qttUper += 1
    else:
        qttLower += 1

# print(qttLower, qttUper)

if(qttLower >= qttUper):
    print(palavra.lower())
else:
    print(palavra.upper())
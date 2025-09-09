n = int(input())

str = list(input())

qtt ={
    "1": 0,
    "0": 0
}

for i in str:
    try:
        qtt[i] += 1
    except:
        qtt[i] = 1

def mod(n):
    if(n < 0):
        n *= -1

    return n

print(mod(qtt["1"] - qtt["0"]))
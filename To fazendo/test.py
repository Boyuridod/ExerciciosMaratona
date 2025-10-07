N = int(input())

def calc(a):
    if(a == 'A'):
        return 10
    elif(a == '2'):
        return 2
    elif(a == '3'):
        return 3
    elif(a == '4'):
        return 4
    elif(a == '5'):
        return 5
    elif(a == '6'):
        return 6
    elif(a == '7'):
        return 7
    elif(a == '8'):
        return 8
    elif(a == '9'):
        return 9
    elif(a == 'J'):
        return 10
    elif(a == 'Q'):
        return 10
    elif(a == 'K'):
        return 10
    elif(a == 'T'):
        return 10
    else:
        return 10


for i in range(N):
    a = input().split(" ")

    aux = a[27:52]

    a = a[0:27]
    # print(a)

    val = calc(a[26][0])
    Y = val

    a = a[0:26-(10-val)]

    # print(a)

    val = 10-val+1

    val2 = calc(a[26-val][0])
    Y += val2

    a = a[0:(26-val+1)-(11-val2)]
    # print(a)

    val2 = 10-val2+1

    val3 = calc(a[26-val-val2][0])
    Y += val3

    a = a[0:(26-val-val2+1)-(11-val3)]
    # print(a)

    a = a + aux
    # print(a)
    
    print(f'Case {i+1}: {a[Y-1]}')
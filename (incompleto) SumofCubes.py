cubos = {}

def achaCubos(lim, cubos):
    i = 0
    cb = 0
    while(cb < lim):
        cb = i * i * i
        if(i not in cubos):
            cubos[i] = i * i * i

        i += 1

def isTrue(x):
    cont = 0

    i = int()

    while(i > 0):

        x -= cubos[i]

        cont += 1

        if(cont >= 2):
            break

        if(x >= cubos[i]):
            i += 1

        i -= 1

    if(x == 0 and cont >= 2):
        return "YES"
    
    return "NO"

def exercicio():
    x = int(input())

    achaCubos(x, cubos)

    print(isTrue(x))
    

t = int(input())

while(t > 0):

    exercicio()

    t -= 1
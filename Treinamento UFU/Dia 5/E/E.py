A = B = M = 1

A, B, M = map(int, input().split(" "))

while(A != 0 and B != 0 and M != 0):

    res = (A + B) % M
    
    print(A, "+", B, "mod", M, "=", res)

    res = (A - B) % M
    
    print(A, "-", B, "mod", M, "=", res)

    res = (A * B) % M
    
    print(A, "*", B, "mod", M, "=", res)

    A, B, M = map(int, input().split(" "))
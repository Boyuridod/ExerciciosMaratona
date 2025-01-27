import math

V, N = input().split(" ")
V = int(V)
N = int(N)

V *= N

# JEITO 1 (ERRADO)

# for i in range(1,9):
#     N = V * (i / 10)

#     if(N % int(N) != 0):
#         print(int(N) + 1, end=" ")

#     else:
#         print(int(N), end=" ")

# N = V * (9 / 10)

# if(N % int(N) != 0):
#     print(int(N) + 1)

# else:
#     print(int(N))

# JEITO 2

# print(math.ceil(V * 0.1), end=" ")
# print(math.ceil(V * 0.2), end=" ")
# print(math.ceil(V * 0.3), end=" ")
# print(math.ceil(V * 0.4), end=" ")
# print(math.ceil(V * 0.5), end=" ")
# print(math.ceil(V * 0.6), end=" ")
# print(math.ceil(V * 0.7), end=" ")
# print(math.ceil(V * 0.8), end=" ")
# print(math.ceil(V * 0.9))

# JEITO 3

for i in range(1,9):
    N = math.ceil(V * (i / 10))
    
    print(N, end=" ")

N = math.ceil(V * (9 / 10))

if(N % int(N) != 0):
    print(N + 1)

else:
    print(N)
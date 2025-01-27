import math

X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())

X1 = (X2 - X1) ** 2
Y1 = (Y2 - Y1) ** 2

X1 = math.sqrt(X1 + Y1)

print(f"{X1:.3f}")
import math
import numpy as np

X, Y, Z = input().split(" ")

X = int(X)
Y = int(Y)
Z = int(Z)

X = np.power(X, Y)

print(X % Z)
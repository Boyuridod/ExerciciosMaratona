Q1 = input().split(" ")
Q2 = input().split(" ")

for i in range(3):
    Q1[i] = int(Q1[i])
    Q2[i] = int(Q2[i])

if((Q1[0] / Q2[0]) == (Q1[1] / Q2[1])):
    print("sistema indeterminado")

else:
    aux = Q1[0] / Q2[0]

    for i in range(3):
        Q2[i] *= aux
        Q2[i] -= Q1[i]

    Q2[2] /= Q2[1]

    Q2[1] = 1

    aux = (Q1[2] - (Q1[1] * Q2[2])) / Q1[0]

    print(f"{aux:.2f} {Q2[2]:.2f}")
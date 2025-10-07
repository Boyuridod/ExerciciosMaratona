T = """I love CS3233 Competitive
Programming. i also love
AlGoRiThM
.......you must stop after reading this line as it starts with 7 dots
after the first input block, there will be one loooooooooooong line..."""

dots = 0
cont = 0

for i in range(len(T)):
    if(dots == 7):
        print(T[i], end="")
        cont += 1
        continue

    if(T[i] == "."):
        dots += 1
    else:
        dots = 0

print(f"Após os \"........\" temos {cont} caracteres")
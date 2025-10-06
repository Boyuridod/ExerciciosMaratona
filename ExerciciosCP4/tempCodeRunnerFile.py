# T = input()
T = "I love CS3233 Competitive Programming. i also love AlGoRiThM"

# palavra = input()
palavra = "love"

pos = 0

ind = []

pos = T.find(palavra, pos + 1)

while(pos != -1):
    ind.append(pos)
    pos = T.find(palavra, pos + 1)

    print("a")

if(len(ind) > 0):
    for i in range(len(ind)):
        if(i < len(ind) - 1):
           print(f"{ind[i]}, ", end="")
        else:
            print(f"{ind[i]}.")
else:
    print(-1)
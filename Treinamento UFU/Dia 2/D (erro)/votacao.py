N = int(input())

cafeterias = []

for i in range(N):
    cafe = input()

    for i in range(len(cafeterias)):

        if(cafe not in cafeterias[i]):
            cafeterias.append([cafe, 1])

        else:
            print(cafeterias[i].index(cafe))
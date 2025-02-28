import pyperclip

ele = []

saida = "vector<int> quadrado = ["

for i in range(1, 1000, 2):
# for i in range(1, 10, 2):
    try:
        ele.append(ele[-1] + i)
    except:
        ele.append(1)

for i in ele:
    saida += f"{i}, "

saida += "};"

print(saida)
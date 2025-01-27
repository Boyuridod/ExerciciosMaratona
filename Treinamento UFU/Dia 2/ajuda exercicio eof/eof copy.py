linhas = []

while True:
    entrada = input("Digite uma linha (ou pressione Enter para encerrar): ")

    if not entrada:
        # Se a entrada estiver vazia, encerra o loop
        break

    linhas.append(entrada)

# Processa as linhas lidas (substitua isso pelo seu código)
print("Linhas lidas:")
for i, linha in enumerate(linhas, start=1):
    print(f"{i}. {linha}")

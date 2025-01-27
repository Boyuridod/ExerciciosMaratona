def buscar_palavra(matriz, palavra):
    direcoes = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Horizontal, Vertical, Diagonal, Diagonal Reversa

    for i in range(10):
        for j in range(10):
            for direcao in direcoes:
                for invertida in [False, True]:  # Verifica a palavra normal e invertida
                    encontrada = True
                    for k in range(len(palavra)):
                        ni, nj = i + k * direcao[0], j + k * direcao[1]
                        if not (0 <= ni < 10 and 0 <= nj < 10) or matriz[ni][nj] != palavra[k] if not invertida else palavra[len(palavra) - 1 - k]:
                            encontrada = False
                            break
                    if encontrada:
                        return 1

    return 0

# Lê a matriz de letras
matriz = [input().split() for _ in range(10)]

# Lê as palavras a serem procuradas
palavras = []
try:
    while True:
        palavra = input()
        palavras.append(palavra)
except EOFError:
    pass

# Procura cada palavra e imprime o resultado
for palavra in palavras:
    resultado = buscar_palavra(matriz, palavra)
    print(resultado)

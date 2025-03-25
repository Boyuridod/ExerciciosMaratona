def crivo_de_eratostenes(n):
    numeros = [True] * (n + 1)
    numeros[0] = numeros[1] = False
    primos = []
    
    for numero, primo in enumerate(numeros):
        if primo:
            primos.append(numero)
            for i in range(numero * 2, n + 1, numero):
                numeros[i] = False
    
    return primos

def salvar_primos_em_txt(n, nome_arquivo="primos.txt"):
    primos = crivo_de_eratostenes(n)
    with open(nome_arquivo, "w") as arquivo:
        for primo in primos:
            arquivo.write(f"{primo}\n")
    print(f"Os números primos até {n} foram salvos em {nome_arquivo}")

# Exemplo de uso
salvar_primos_em_txt(100)

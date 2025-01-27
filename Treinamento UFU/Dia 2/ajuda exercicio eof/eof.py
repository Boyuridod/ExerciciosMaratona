# Abre o arquivo para leitura
with open('exemplo.txt', 'r') as arquivo:
    # Loop para ler linhas do arquivo
    while True:
        linha = arquivo.readline()

        # Verifica se a linha é vazia, indicando o final do arquivo
        if not linha:
            break

        # Processa a linha (substitua isso pelo seu código)
        print(linha.strip())  # strip() remove espaços em branco e quebras de linha

print("Fim do arquivo alcançado.")

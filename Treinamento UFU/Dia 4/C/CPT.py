from itertools import permutations

def eh_consoante(letra):
    return letra not in "AEIOU"

def gerar_anagramas(entrada):
    entrada = entrada.replace(" ", "").upper()  # Remover espaços e converter para maiúsculas
    consoantes = [letra for letra in entrada if eh_consoante(letra)]
    vogais = [letra for letra in entrada if not eh_consoante(letra)]
    
    # Gerar todas as permutações de consoantes e vogais
    permutacoes_consoantes = set(permutations(consoantes))
    permutacoes_vogais = set(permutations(vogais))
    
    # Inicializar o contador de anagramas
    total_anagramas = 0
    
    # Para cada permutação de consoantes e vogais, verifique as regras e conte os anagramas válidos
    for consoante_perm in permutacoes_consoantes:
        for vogal_perm in permutacoes_vogais:
            anagrama = "".join([c + v for c, v in zip(consoante_perm, vogal_perm)])
            total_anagramas += 1
    
    return total_anagramas

# Exemplo de uso:
entrada = input()
resultado = gerar_anagramas(entrada)
print(resultado)
import random

# Gera 10^5 linhas contendo 2 números inteiros entre 1 e 10^5
for _ in range(10**5):
    numero1 = random.randint(1, 10**5)
    numero2 = random.randint(1, 10**5)
    print(numero1, numero2)

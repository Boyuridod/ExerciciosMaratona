# https://vjudge.net/problem/Gym-105327K
# https://vjudge.net/contest/747064#problem/K
# https://codeforces.com/problemset/gymProblem/105327/K

N = int(input())

a = list(map(int, input().split(" ")))

al = []
bo = []

ordem = []

a.sort(reverse=True)

if(sum(a) % 2 != 0):
    print(-1)

else:
    for i in a:
        if(sum(al) > sum(bo)):
            bo.append(i)
        else:
            al.append(i)

        ordem.append(i)

    if(sum(al) == sum(bo)):
        for i in ordem:
            print(i, end=" ")

    else:
        print(-1)

# # solução em Python 3
# import sys

# def solve():
#     data = sys.stdin.read().strip().split()
#     if not data:
#         return
#     it = iter(data)
#     n = int(next(it))
#     a = [int(next(it)) for _ in range(n)]
#     S = sum(a)
#     if S % 2 == 1:
#         print(-1)
#         return
#     target = S // 2

#     # DP para subset sum com reconstrução
#     # dp[s] = index of last used item to achieve sum s (or -1 if unreachable), base dp[0] = -2 (marcador)
#     dp = [-1] * (target + 1)
#     dp[0] = -2
#     # armazenar predecessor (para reconstruir): prev[s] = (previous_sum, index)
#     prev = [None] * (target + 1)

#     for idx, val in enumerate(a):
#         # iterar soma de trás pra frente
#         for s in range(target, val - 1, -1):
#             if dp[s] == -1 and dp[s - val] != -1:
#                 dp[s] = idx
#                 prev[s] = s - val

#     if dp[target] == -1:
#         print(-1)
#         return

#     # reconstruir indices do subconjunto que somam target (Alice)
#     alice_indices = set()
#     s = target
#     while s != 0:
#         idx = dp[s]
#         alice_indices.add(idx)
#         s = prev[s]

#     # separar valores em duas listas (mantendo apenas valores, não índices)
#     alice_vals = []
#     bob_vals = []
#     for i, val in enumerate(a):
#         if i in alice_indices:
#             alice_vals.append(val)
#         else:
#             bob_vals.append(val)

#     # ordenar decrescente e fazer merge conforme regras
#     alice_vals.sort(reverse=True)
#     bob_vals.sort(reverse=True)

#     sumA = 0
#     sumB = 0
#     ia = 0
#     ib = 0
#     order = []

#     while ia < len(alice_vals) or ib < len(bob_vals):
#         if ia < len(alice_vals) and (ib >= len(bob_vals) or sumA <= sumB):
#             order.append(alice_vals[ia])
#             sumA += alice_vals[ia]
#             ia += 1
#         else:
#             order.append(bob_vals[ib])
#             sumB += bob_vals[ib]
#             ib += 1

#     # opcional: verificar que funcionou
#     # simular distribuição para garantir (pode comentar depois)
#     A = 0
#     B = 0
#     for x in order:
#         if A <= B:
#             A += x
#         else:
#             B += x
#     if A != B:
#         # como fallback (raro), imprimir -1
#         print(-1)
#         return

#     print(" ".join(map(str, order)))

# if __name__ == "__main__":
#     solve()

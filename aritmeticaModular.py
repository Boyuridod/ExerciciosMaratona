mod = 1e9 + 7

x, op, y = input().split(" ")

x = int(x)
y = int(y)

match op:
    case "+":
        print(int((x + y) % mod))

    case "-":
        print(int(((x - y) + mod) % mod))

    case "*":
        print(int((x * y) % mod))

    case "^":
        res = 1

        for i in range (y):
            res = (res * x) % mod

        print(int(res))
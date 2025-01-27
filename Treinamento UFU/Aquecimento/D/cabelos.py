E = float(input())

G = float(input())

porcen = (E / G) * 100

if(porcen < 73):
    print("ETANOL")

else:
    print("GASOLINA")
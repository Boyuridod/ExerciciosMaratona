import decimal

E, V = map(int, input().split(" "))

minutos = ((E / V)) * 60

hora = int(minutos / 60)

print(minutos, (hora * 60))
minuto = minutos - (hora * 60)

print(hora + 19, minuto)
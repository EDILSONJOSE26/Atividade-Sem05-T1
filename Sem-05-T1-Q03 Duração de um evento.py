segundos = int(input())

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60
print("{}:{}:{}".format(horas,minutos,segundos))

horas = int(input("Informe quantas horas você correu: "))
minutos = int(input("Informe também a quantidade de minutos: "))
segundos = int(input("E a quantidade de segundos: "))

horas_seg = horas * 3600
minutos_seg = minutos * 60

total_seg = horas_seg + minutos_seg + segundos
print(f"Você correu um total de {total_seg} segundos hoje")

tarifa_km = 2.5
tarifa_dias = 10

quilometros = float(input("Quantos quilômetros você rodou?\n"))
dias_alugado = int(input("Quantos dias ficou com o carro?\n"))

total = (quilometros * tarifa_km) + (dias_alugado * tarifa_dias)

print(f"Você ira pagar R$ {total:.2f} pelo aluguel do carro.")

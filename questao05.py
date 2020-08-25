salario = float(input("Informe o salário que você recebe:\nR$ "))

if salario <= 1045:
    percentual = '20%'
    aumento = 0.2 * salario
elif (salario >= 1045.01) and (salario <= 2015):
    percentual = '15%'
    aumento = 0.15 * salario
elif (salario >= 2015.01) and (salario <= 3250):
    percentual = '10%'
    aumento = 0.1 * salario
elif (salario >= 3250.01):
    percentual = '5%'
    aumento = 0.05 * salario

print(f"Salário antes do reajuste: R$ {salario}")
print(f"Percentual do reajuste: {percentual}")
print(f"Valor do aumento: R$ {aumento}")
print(f"Novo salário: R$ {salario + aumento}")

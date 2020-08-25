from datetime import datetime

nasceu = int(input("Em que ano você nasceu?\n"))
peso = float(input("Quanto você pesa?\n"))
dormiu = int(input("Que horas você dormiu?\n"))
acordou = int(input("Que hora você acordou?\n"))

idade = datetime.now().year - nasceu
descanso = (24 - dormiu) + acordou

if (idade >= 16) and (idade <= 69):
    if (peso > 50):
        if descanso >= 6:
            print("Você está pronto para doar sangue!")
        else:
            print("Você precisa ter dormido pelo menos 6hrs nas ultimas 24hrs!")
    else:
        print("Neste momento você está abaixo do peso recomendado para um doador!")
else:
    print("É preciso ter entre 16 e 69 anos para estar apto a doar sangue!")

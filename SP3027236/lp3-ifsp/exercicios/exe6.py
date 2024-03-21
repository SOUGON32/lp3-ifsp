def calcular_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def calcular_filtragem_por_hora(volume):
    return volume * 2  

comprimento = float(input("Digite o comprimento do aquário em centímetros: "))
altura = float(input("Digite a altura do aquário em centímetros: "))
largura = float(input("Digite a largura do aquário em centímetros: "))
temperatura_desejada = float(input("Digite a temperatura desejada em graus Celsius: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente em graus Celsius: "))

volume = calcular_volume(comprimento, altura, largura)
potencia_termostato = calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)
filtragem_por_hora = calcular_filtragem_por_hora(volume)

print("Volume do aquário: {:.2f} litros".format(volume))
print("Potência do termostato necessária: {:.2f} watts".format(potencia_termostato))
print("Quantidade de filtragem por hora necessária: {:.2f} litros/hora".format(filtragem_por_hora))

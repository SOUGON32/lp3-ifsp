def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25.0:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Excesso de peso"
    elif 30.0 <= imc < 35.0:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc < 40.0:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")

if imc < 18.5:
    peso_ideal = 24.9 * (altura ** 2)
    peso_diferenca = peso_ideal - peso
    print(f"Você precisa ganhar {abs(peso_diferenca):.2f} Kg para atingir o peso normal.")
elif imc >= 25.0:
    peso_ideal = 24.9 * (altura ** 2)
    peso_diferenca = peso - peso_ideal
    print(f"Você precisa perder {peso_diferenca:.2f} Kg para atingir o peso normal.")

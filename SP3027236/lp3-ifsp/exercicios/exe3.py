
faixas_desconto = {
    (0.01, 9.99): 0,
    (10.00, 99.99): 5,
    (100.00, 499.99): 10,
    (500.00, float("inf")): 15,
}


valor_compra = float(input("Digite o valor da compra: "))


for faixa, desconto in faixas_desconto.items():
    if valor_compra >= faixa[0] and valor_compra <= faixa[1]:
        desconto_aplicado = valor_compra * desconto / 100
        break


valor_final = valor_compra - desconto_aplicado
print(f"Valor final: R${valor_final:.2f}")
print(f"Desconto aplicado: {desconto:.0f}%")

PRECO_POR_KM_REAIS_ATE_250_KM = 0.5
PRECO_POR_KM_REAIS_MAIS_250_KM = 0.45

distanciaKm = float(input("Digite a distância em quilômetros: "))

if distanciaKm <= 250:
    preco = distanciaKm * PRECO_POR_KM_REAIS_ATE_250_KM
else:
    preco = distanciaKm * PRECO_POR_KM_REAIS_MAIS_250_KM

print(f"O preço da viagem é R$ {preco:.2f}")
n = int(input("Digite o número de pessoas: "))

pessoas = []

for i in range(n):
    nome = input("Digite o nome da pessoa " + str(i + 1) + ": ")
    idade = float(input("Digite o idade da pessoa " + str(i + 1) + ": "))
    sexo = input("Digite o sexo da pessoa " + str(i + 1) + " (M ou F): ")
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

mulheres_com_menos_de_vinte_anos = 0
idade_acumulado = 0

for pessoa in pessoas:
    idade_acumulado += pessoa["idade"]

    if (pessoa["sexo"] == "F" and pessoa["idade"] < 20):
        mulheres_com_menos_de_vinte_anos += 1

print("Quantidade de mulheres com menos de vinte anos: ", mulheres_com_menos_de_vinte_anos)
print("Média das idades: ", idade_acumulado / len(pessoas))
pessoas = []

for i in range(3):
    nome = input("Digite o nome da pessoa " + str(i + 1) + ": ")
    peso = float(input("Digite o peso da pessoa " + str(i + 1) + ": "))
    pessoas.append({"nome": nome, "peso": peso})

mais_leve = pessoas[0]
mais_pesada = pessoas[0]

for pessoa in pessoas:
    if pessoa["peso"] < mais_leve["peso"]:
        mais_leve = pessoa
    if pessoa["peso"] > mais_pesada["peso"]:
        mais_pesada = pessoa

print("Pessoa mais leve:", mais_leve["nome"], "com", mais_leve["peso"], "kg")
print("Pessoa mais pesada:", mais_pesada["nome"], "com", mais_pesada["peso"], "kg")

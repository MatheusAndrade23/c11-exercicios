numero = int(input("Digite um número: "))
intervaloCima = int(input("Digite o limite superior do intervalo: "))
intervaloBaixo = int(input("Digite o limite inferior do intervalo: "))
print("Vou calcular a tabuada do número", numero, "entre", intervaloBaixo, "e", intervaloCima)

print("A tabuada de", numero, "é:")
for i in range(intervaloBaixo, intervaloCima + 1):
    print(numero, "x", i, "=", numero * i)

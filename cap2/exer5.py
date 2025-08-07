numero = int(input("Digite um número entre 1000 e 9999: "))

print("Esse é o número da unidade:", numero % 10)
print("Esse é o número da dezena:", (numero // 10) % 10)
print("Esse é o número da centena:", (numero // 100) % 10)
print("Esse é o número do milhar:", (numero // 1000) % 10)
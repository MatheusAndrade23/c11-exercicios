while True:
    sexo = input("Digite seu sexo (M/F): ")
    if sexo == "M":
        print("Você é homem.")
        break
    elif sexo == "F":
        print("Você é mulher.")
        break
    else:
        print("Opção inválida. Por favor, digite M para Masculino ou F para Feminino.")
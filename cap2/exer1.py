nome = input("Digite seu nome: ")

print("Seu nome em letra maiúscula é:", nome.upper())
print("Seu nome em letra minúscula é:", nome.lower())
print("O comprimento do seu nome é:", len(nome))
print("Como seria se trocasse seu último nome por 'inatel':", nome.replace(nome.split()[-1], "inatel"))
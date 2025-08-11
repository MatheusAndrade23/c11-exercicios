aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["nota"] = int(input("Digite a nota do aluno: "))

if(aluno["nota"] >= 50):
    aluno["situacao"] = "AP"
else: 
    aluno["situacao"] = "RP"

print(aluno.items())
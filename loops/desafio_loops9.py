alunos = {}
while True:
    nome = input("Informe o seu nome: ")
    if nome == 'sair':
        break
    nota = int(input("Informe a sua nota: "))
    alunos[nome] = nota
print(alunos)
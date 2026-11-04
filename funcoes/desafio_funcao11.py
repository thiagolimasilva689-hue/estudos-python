def nome(nome, msg):
    return f"{nome} {msg}"


def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento


nome_usuario = input("Nome: ")
mensagem = input("Mensagem: ")

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

idade = calcular_idade(ano_nascimento, ano_atual)

print(nome(nome_usuario, mensagem))
print("Idade:", idade)

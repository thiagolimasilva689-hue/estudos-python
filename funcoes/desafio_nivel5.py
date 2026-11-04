dicionario = {}
while True:
    informe= input("Informe o seu nome: ")
    if informe == 'Fim':
        break
    idade = int(input("Informe a sua idade: "))
    dicionario[informe] = idade
print(dicionario)
        


"""
Exercício 1 — Função de saudação
Crie uma função chamada saudacao que recebe um nome e imprime:

text
"Olá, [nome]! Seja bem-vindo(a)!"
Exemplo:

python
saudacao("Thiago")
"""
def saudação(nome):
    return f"Olá,{nome}! Seja bem-vindo(a)!"
#nome = input("INFORME O SEU NOME: ")

"""
Exercício 2 — Função com retorno
Crie uma função chamada calcular_media que recebe 3 notas e retorna a média.

Exemplo:

python
media = calcular_media(7, 8, 9)
print(media)
# Saída: 8.0
"""
def calcular_media(a,b,c):
    media = (a + b + c) / 3
    return media
#print(calcular_media(7,8,9))


"""
Exercício 3 — Função com condicional
Crie uma função chamada classificar_idade que recebe uma idade e retorna:

"Criança" se idade < 12

"Adolescente" se 12 <= idade < 18

"Adulto" se idade >= 18
"""
def classificar_idade(idade):
    if idade <=12:
        return "Criança"
    elif idade > 12 and idade <18:
        return "Adolescente"
    elif idade >= 18 and idade <= 64:
        return "Adulto"
    else:
        return "Idoso"
'''

Exercício 4 — Função com lista
Crie uma função chamada maior_numero que recebe uma lista de números e retorna o maior deles.

Exemplo:

python
lista = [5, 12, 8, 20, 3]
print(maior_numero(lista))
# Saída: 20
def maior_numero(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior =  i
    return maior
num = int(input("INFORMER UM NÚMERO: "))
lista = []
while True:
    num = int(input("INFORME UM NÚMERO: "))
    if num == -0:
               break
    lista.append(num)
print(maior_numero(lista))
'''


"""
Exercício 5 — Função com dicionário
Crie uma função chamada total_precos que recebe um dicionário de produtos (nome: preço) e retorna a soma de todos os preços.

Exemplo:

python
produtos = {
    "Arroz": 25.90,
    "Feijão": 10.50,
    "Carne": 45.00
}
print(total_precos(produtos))
# Saída: 81.40
"""
def total_precos(produtos):
    return sum(produtos.values())
produtos = {
    "Arroz": 25.90,
    "Feijão": 10.50,
    "Carne": 45.00
}
print(total_precos(produtos))
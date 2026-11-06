"""
Exercício 1 de 3 — Identificar números pares
Objetivo: praticar listas, laço for, condição if e o operador % em Python.
Imagine que você recebeu esta lista de números:
numeros = [3, 8, 11, 14, 20, 7, 9, 12]
Sua tarefa é criar um programa que percorra a lista e mostre somente os números pares, um por linha.
O resultado esperado é:
8
14
20
12
Dica para pensar
- for permite percorrer os números da lista, um de cada vez.
- if permite verificar uma condição.
- O operador % calcula o resto de uma divisão. Por exemplo, um número par dividido por 2 tem resto zero.
numeros = [3, 8, 11, 14, 20, 7, 9, 12]
for num in numeros:
    if num % 2 == 0:
        print(num)
"""

"""
Exercício 2 de 3 — Encontrar o maior e o menor número
Agora vamos praticar funções, parâmetros, listas e return.

Considere esta lista:
numeros = [12, 5, 27, 3, 18]
Sua tarefa é criar uma função chamada maior_menor(lista) que receba uma lista e retorne o maior e o menor número.
O resultado esperado é:
Maior: 27
Menor: 3
Dicas para pensar:
- def cria uma função.
- lista será o parâmetro que recebe os números.
- Você pode usar max(lista) para encontrar o maior e min(lista) para encontrar o menor.
- Use return para devolver os resultados.
- Depois, chame a função e mostre os resultados com print().
"""
numeros = [12, 5, 27, 3, 18]
def  maior_menor(numeros:list[int]):
    maior = f"Maior:{max(numeros)}"
    menor = f"Menor:{min(numeros)}"
    return maior,menor
maior,menor = maior_menor(numeros)
#print(maior)
#print(menor)

"""
Exercício 3 de 3 — Somar preços com uma função
Agora vamos avaliar se você consegue aplicar funções a outro problema.
Considere esta lista:
precos = [12.50, 8.00, 15.75, 4.25]
Sua tarefa é criar uma função chamada somar_precos(lista) que receba a lista e retorne a soma de todos os preços.
Resultado esperado:
"""
def somar_precos(lista:list[float])-> float:
    total = sum(lista)
    return total
precos = [12.50, 8.00, 15.75, 4.25]
resultado = somar_precos(precos)
print(f"Total : {resultado}")
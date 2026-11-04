"""
Exercício 2 (lista + filtro)

Dada a lista:

numeros = [3, 8, 15, 22, 7, 30, 11]

👉 Faça um programa que:

crie uma nova lista só com números maiores que 10
mostre essa nova lista
mostre quantos números foram filtrados
"""
lista =[]
numeros = [3, 8, 15, 22, 7, 30, 11]
for i in numeros:
    if i>10:
        lista.append(i)
print(lista)
print(f"Quantidade : {len(lista)}")
"""
 Exercício 4 (nível mais importante 🔥)

Peça números ao usuário até ele digitar 0.

👉 Depois:

guarde todos em uma lista
mostre:
o maior número
o menor número
a média
quantos números são maiores que a média
"""
lista =[]
while True:
    num = int(input("Informe um número: "))
    if num == 0:
        break
    lista.append(num)
maior = max(lista)
menor = min(lista)
media = sum(lista) / len(lista)

acima_media = 0
for i in lista:
    if i > media:
        acima_media += 1
print("Lista:", lista)
print("Maior:", maior)
print("Menor:", menor)
print("Média:", media)
print("Maiores que a média:", acima_media)
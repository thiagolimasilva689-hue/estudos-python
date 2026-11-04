"""
Exercício 4 — Média de lista
Crie uma função media_lista(lista) que recebe uma lista de números e retorna a média. Se a lista estiver vazia, retorne 0.

python
print(media_lista([5, 10, 15]))  # 10.0
print(media_lista([]))           # 0
"""
def media_lista(lista):
    if len(lista) == 0:
        return 0
    media = sum(lista) / len(lista)
    return media
lista = []
while True:
    num = int(input("Informe um número: "))
    if num == -1:
        break
    lista.append(num)
resultado = media_lista(lista)
print(resultado)
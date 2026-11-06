"""
Exercício 2 — Remover duplicatas 

Crie uma função remover_duplicatas(lista) que retorna uma nova lista sem itens repetidos. 

python 

print(remover_duplicatas([1, 2, 2, 3, 3, 3]))  # [1, 2, 3] 
"""
def remover_duplicatas(lista):
    nova = []
    for item in lista:
        if item not in nova:
            nova.append(item)
    return nova

print(remover_duplicatas([1, 2, 2, 3, 3, 3]))


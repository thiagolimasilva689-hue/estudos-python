"""
Exercício 5 — Filtrar maiores que
Crie uma função filtrar_maiores(lista, valor) que recebe uma lista e um valor, e retorna uma nova lista apenas com os números maiores que o valor.

python
print(filtrar_maiores([3, 7, 2, 9, 5], 4))  # [7, 9, 5]
"""
def filtrar_maiores(lista, valor):
    resultado = []              # lista vazia
    for num in lista:           # percorre cada número
        if num > valor:         # se for maior
            resultado.append(num)  # adiciona
    return resultado  
    
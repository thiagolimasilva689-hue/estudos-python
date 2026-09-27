"""
Exercício 4 — Total da lista com taxa
Crie uma função total_pedido(itens, taxa) que recebe uma lista de preços e uma taxa de entrega, e retorna o total (soma dos itens + taxa).
"""
def total_pedido(itens, taxa):
    total = 0
    for i in itens:
        total += i
    total += taxa
    return total
print(total_pedido([25, 10, 15], 5))
 
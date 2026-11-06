"""
Exercício 4 — Filtrar pares e ímpares
Crie uma função separar(lista) que recebe uma lista de números e retorna duas listas: uma com os pares e outra com os ímpares.

python
pares, impares = separar([1, 2, 3, 4, 5, 6])
print(pares)    # [2, 4, 6]
print(impares)  # [1, 3, 5
"""
def separar(lista):
    par_lista = []
    impar_lista = []
    for num in lista:
        if num % 2 == 0 :
            par_lista.append(num)
        else:
            impar_lista.append(num)
    return par_lista,impar_lista
print(separar([1, 2, 3, 4, 5, 6]))
    
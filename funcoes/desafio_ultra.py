"""
Exercício 2 — Números pares

Crie uma função filtrar_pares que recebe uma lista de números e retorna uma nova lista apenas com os pares.

Exemplo:

python
print(filtrar_pares([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]

"""

def filtrar_pares(lista):
    par = []
    for num in lista:
        if num % 2 == 0:
            par.append(num)
    return par
#print(filtrar_pares([1, 2, 3, 4, 5, 6]))

"""
Exercício 3 — Fatorial

Crie uma função fatorial que recebe um número inteiro positivo e retorna o fatorial dele.

Exemplo:

python
print(fatorial(5))  # 120 (5 × 4 × 3 × 2 × 1)
print(fatorial(3))  # 6
"""
def fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado = resultado * i
    return resultado

"""



"""
    
    


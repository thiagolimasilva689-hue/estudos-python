"""
Exercício 1 — Maior de três
Crie uma função maior_de_tres(a, b, c) que recebe três números e retorna o maior deles.

python
print(maior_de_tres(5, 9, 3))  # 9
"""
def maior(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
lista = []
for num in range(0,3):
    num = int(input("Digitei um numero: "))
    lista.append(num)
definir = maior(lista[0],lista[1],lista[2])
print(definir)
"""
Exercício 2 — Média de notas por aluno
Dado o dicionário:

python
alunos = {
    "Thiago": [8.7, 6.5],
    "Ana": [7.8, 8.5],
    "Luis": [4.5, 7.5]
}
Mostre a média de cada aluno. Se a média for ≥ 6, diga "Aprovado". Senão, "Reprovado".
"""
alunos = {
    "Thiago": [8.7, 6.5],
    "Ana": [7.8, 8.5],
    "Luis": [4.5, 7.5]
}
def situaca_aluno(alunos:dict)->None:
    """
    Função que analisar a Media dos alunos
    Args:
         analisar O dicionario
    Returns:
            Retornar O Resultando
    """
    for nome,notas in alunos.items():
        Media = sum(notas)/ len(notas)
        print(f"A {nome} e sua Media é {Media:.2f}")
        if Media >= 6:
            print(f"{nome} Foi aprovador!")
        else:
            print(f"{nome} foi reprovador")

"""
Exercício 3 — Função com validação
Crie uma função calcular_desconto(valor, percentual) que:
Só aceita valor > 0
Só aceita percentual entre 0 e 100
Retorna o valor com desconto
Se algum valor for inválido, retorna "Valor inválido"
Exemplo de uso:
python
print(calcular_desconto(100, 10))   # deve retornar 90.0
print(calcular_desconto(100, 150))  # deve retornar "Valor inválido"
print(calcular_desconto(-50, 10))   # deve retornar "Valor inválido"
"""
def validacao(valor, percentual):
    if valor <= 0 or (percentual < 0  or percentual > 100):
         return "Valor inválido"
    else:
        return valor - (valor * percentual / 100)

"""
Exercício 4 — Classe Produto
Crie uma classe Produto com:
Atributos: nome, preco, quantidade
Método valor_total() que retorna preco * quantidade
Método mostrar_dados() que imprime nome, preço, quantidade e valor total
Depois crie 2 produtos e chame mostrar_dados().
"""
class Produto:
    def __init__(self,nome:str,preco:float,quantidade:int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def valor_total(self):
        return self.preco * self.quantidade
    def mostrar_dados(self):
        print(f"PRODUTO : {self.nome}")
        print(f"O SEU PREÇO : {self.preco}")
        print(f"A QUANTIDADE DO PRODUTO: {self.quantidade}")
        print(f"O VALOR TOTAL DO PRODUTO É {self.valor_total():.2f}")
Produto1 = Produto("Nescau",18.7,4)
produto2 = Produto("Arroz", 25.90, 3)


"""
Exercício 5 — Loop com while e lista
Peça números ao usuário até ele digitar 0. Guarde os números em uma lista e, no fim, mostre:

A lista completa

O maior número

O menor número

A média

Exemplo de entrada:

text
5
8
3
0
Saída esperada:

text
Lista: [5, 8, 3]
Maior: 8
Menor: 3
Média: 5.33
"""
lista = []
while True:
    num = int(input("INFORME UM NÚMERO:"))
    if num == 0:
        break
    lista.append(num)
if len(lista) > 0:
    print(f"Lista: {lista}")
    print(f"Maior: {max(lista)}")
    print(f"Menor: {min(lista)}")
    print(f"Média: {(sum(lista)/len(lista)):.2f}")
else:
    print("Nenhum número informado.")
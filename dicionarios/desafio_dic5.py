"""
Exercício 5 — Filtro por valor 

Crie uma função que recebe um dicionário de produtos e preços, e um valor máximo. Retorne um novo dicionário apenas com os produtos abaixo desse valor. 

python 

produtos = {"Arroz": 25, "Feijão": 10, "Carne": 40, "Leite": 6} 
print(filtrar_baratos(produtos, 20)) 
# {'Feijão': 10, 'Leite': 6} 


"""
produtos = {"Arroz": 25, "Feijão": 10, "Carne": 40, "Leite": 6} 
def filtrar_baratos(produtos, valor):
    dic = {}
    for nome, preco in produtos.items():
        if preco < valor:
            dic[nome] = preco
    return dic
print(filtrar_baratos(produtos,20))
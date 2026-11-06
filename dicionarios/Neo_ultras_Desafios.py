"""
Questão 1 — Dicionário + Função (básico)
Enunciado: Crie uma função chamada media_notas que recebe um dicionário onde as chaves são nomes de alunos e os valores são listas de notas. Retorne um novo dicionário com o nome do aluno e a média dele.

Exemplo de entrada:

python
alunos = {
    "Thiago": [8.7, 6.5, 7.0],
    "Ana": [7.8, 8.5, 9.0],
    "Luis": [4.5, 7.5, 5.0]
}
"""
alunos: dict= {
    "Thiago": [8.7, 6.5, 7.0],
    "Ana": [7.8, 8.5, 9.0],
    "Luis": [4.5, 7.5, 5.0]
}
def  media_notas(alunos:dict):
    """
    Calcula a média das notas dos alunos.

    Args:
            alunos: Dicionário com nome do aluno e lista de notas.
    Returns:
            Novo dicionário com nome do aluno e sua média.
"""
    novo_dict : dict = {}
    for nome,notas in alunos.items():
        Media = sum(notas)/len(notas)
        novo_dict[nome]=Media
    return novo_dict
resultado = media_notas(alunos)
for nome, media in resultado.items():
    print(f"{nome}: {media:.2f}")

"""
 Questão 2 — Lista + Função com filtro (intermediário)
Enunciado: Crie uma função chamada filtrar_produtos que recebe uma lista de dicionários (cada dicionário tem nome e preco) e um valor limite. Retorne uma nova lista apenas com os produtos cujo preço é maior ou igual ao limite, ordenados do mais caro para o mais barato.

Exemplo de entrada:

python
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 1200},
    {"nome": "Cadeira", "preco": 800}
]
filtrar_produtos(produtos, 500)
Saída esperada:

python
[
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Monitor", "preco": 1200},
    {"nome": "Cadeira", "preco": 800}
]
"""
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 1200},
    {"nome": "Cadeira", "preco": 800}
]
def filtrar_produtos(produtos:list,valor_limite:float)->list:
    """
    Função para filtrar valores dentro da lista de produtos
    Args:
         Receber a listar
         Analisar os seus valores
    Returns:
            retornar com uma lista com valores filtrados
    """
    nova_lista = []
    for produto in produtos:
        if produto['preco']> valor_limite:
             nova_lista.append(produto)
    return nova_lista

"""
 Questão 4 — Função com validação + dicionário (avançado)
Enunciado: Crie uma função chamada cadastrar_produto que recebe:
Um dicionário estoque (pode estar vazio)
Uma string nome
Um float preco
Um int quantidade
A função deve:
Validar que preco > 0 e quantidade >= 0. Se não, retornar "Erro: valores inválidos".
Validar que o produto não existe no estoque. Se existir, retornar "Erro: produto já cadastrado".
Adicionar o produto ao estoque no formato:
python
{
    "nome": {"preco": preco, "quantidade": quantidade}
}
Retornar o estoque atualizado.
Exemplo de uso:
python
estoque = {}
estoque = cadastrar_produto(estoque, "Notebook", 3500.0, 10)
estoque = cadastrar_produto(estoque, "Mouse", 80.0, 50)
estoque = cadastrar_produto(estoque, "Notebook", 3000.0, 5)  # deve retornar erro
estoque = cadastrar_produto(estoque, "Teclado", -10, 5)  # deve retornar erro
O que treina: validação, dicionário aninhado, in, return, type hints, docstring
"""
estoque = {}

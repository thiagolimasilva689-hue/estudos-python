"""
Exercício 1 — Criar e acessar 

Crie um dicionário com 3 carros e seus preços. Peça ao usuário o nome de um carro e mostre o preço. Se não existir, mostre "Carro não encontrado". 

python 

# Exemplo de uso: 
# Digite o carro: Gol 
# Preço: R$ 45000 
"""
loja = {
    'Toyota Corolla' :  150.000,
    'Fiat Cronos':97.990,
    'chevrolet onix': 101.790
}
pergunta = input("Informe o seu carro:")
if pergunta in loja:
    print(f"Preço: R$ {loja[pergunta]}")
else:
    print("Carro não encontrado")

"""
idade = int(input("Informe a sua idade: "))
    dicionario[informe] = idade
print(dicionario)

"""
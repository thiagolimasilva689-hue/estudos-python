"""
Exercício 2 — Adicionar e remover 

Crie um dicionário vazio. Depois: 

Adicione 3 frutas com seus preços 

Remova uma fruta 

Mostre o dicionário final 
"""

frutas = {}
frutas['Maçã'] = 5.90
frutas['Goiaba'] = 3.50
frutas['Pera'] = 7.20


#Remover 
del frutas['Maçã']

# Mostrar dicionário final
print(frutas)
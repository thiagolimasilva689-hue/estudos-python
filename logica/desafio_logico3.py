"""
Exercício 3 (string + lista)

Peça uma frase ao usuário.

👉 Depois:

transforme tudo em minúsculo
conte quantas vogais existem
guarde cada vogal encontrada em uma lista
mostre a lista de vogais

💡 Exemplo:
"casa" → ['a', 'a']
"""
lista = []
vogal = 0
frase = input("Informe uma frase: ")

for i in frase.lower():
    if i in 'aeiou':
        lista.append(i)
        vogal += 1

print("Vogais encontradas:", lista)
print("Quantidade de vogais:", vogal)


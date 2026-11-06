"""
Exercício 2 — Contar vogais
Crie uma função contar_vogais(frase) que retorna quantas vogais existem na frase.

python
print(contar_vogais("Thiago"))      # 3
print(contar_vogais("Python"))      # 1
print(contar_vogais("AEIOU"))       # 5
"""
def vogais(lentras):
    contar = 0
    for i in lentras:
       if i.lower() in "aeiou":
            contar += 1
    return contar
     
frases =  vogais(input("Informe uma palavra: "))
print(frases)
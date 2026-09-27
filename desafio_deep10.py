""""
Exercício 3 — Contar vogais
Crie uma função contar_vogais(frase) que recebe uma string e retorna quantas vogais ela tem.

python
print(contar_vogais("Thiago"))  # 3
"""
def vogais(lentras):
    contar = 0
    for i in lentras:
        if i in "aeiou":
            contar+=1
    return contar
frases =  vogais(input("Informe uma palavra: "))
print(frases)
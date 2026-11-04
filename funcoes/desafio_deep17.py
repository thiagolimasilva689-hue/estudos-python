"""
Exercício 5 — Classificar nota
Crie uma função classificar(nota) que:

Se nota >= 7, retorna "Aprovado"

Se nota >= 5, retorna "Recuperação"

Caso contrário, retorna "Reprovado"
"""
def Classificar(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
print(Classificar(8))
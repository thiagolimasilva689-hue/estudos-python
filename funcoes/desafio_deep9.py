"""
Exercício 2 — Par ou ímpar
Crie uma função par_ou_impar(numero) que retorna "Par" ou "Ímpar".
"""
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
resultado = par_ou_impar(12)
print(resultado)
        
    

"""
Exercício 5 — Validar CPF (básico) 

Crie uma função validar_cpf(cpf) que recebe uma string com 11 dígitos e retorna True se for válido (todos os dígitos não podem ser iguais e deve ter 11 caracteres). 
"""
def validar_cpf(cpf):
    # 1. Verificar se tem 11 caracteres
    if len(cpf) != 11:
        return False
    
    # 2. Verificar se todos são iguais
    primeiro = cpf[0]
    todos_iguais = True
    for digito in cpf:
        if digito != primeiro:
            todos_iguais = False
            break
    
    if todos_iguais:
        return False
    
    return True

print(validar_cpf("12345678901"))  # True
print(validar_cpf("11111111111"))  # False
print(validar_cpf("123"))          # False
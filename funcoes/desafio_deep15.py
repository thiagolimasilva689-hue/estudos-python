"""
Exercício 3 — Saudação personalizada
Crie uma função saudacao(nome, hora) que:

Se hora < 12, retorna "Bom dia, Thiago!"

Se hora < 18, retorna "Boa tarde, Thiago!"

Caso contrário, retorna "Boa noite, Thiago!"
"""
def Saudação(nome, hora):
    if hora <= 12 :
        return  f"Bom dia, {nome}!"
    elif hora <= 18:
        return (f"Bom tarde, {nome} ")
    else:
        return(f"Bom noite, {nome} ")
hora = int(input("Informe a hora: "))
nome  = input("Informe o seu nome: ")
print(Saudação(nome,hora))
identidade = {
      'Ana':20,
      'João':17,
      'Carlos':25
}
def maiores_idade(idantidade):
    contar = 0
    for idade in idantidade.values():
        if idade > 18:
            contar+=1
    return contar
resultado = maiores_idade(identidade)
print(f"A quantidade maiores de idade: ",resultado)

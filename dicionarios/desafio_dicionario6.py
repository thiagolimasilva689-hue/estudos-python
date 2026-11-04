
pessoas ={
    'João pedro silva':18,
    'Ana vellutini Bettencourt': 20,
    'Thiago de lima brito':22,
    'Paulo gonzales santos':16,
    'renam oliveira': 14,
    'Camila britos dos santos':12,
}
def definir_maior(pessoas):
    contar = 0
    for idade in pessoas.values():
        if idade > 18:
              contar+=1
    return contar
maiores_idade = definir_maior(pessoas)
print(maiores_idade)

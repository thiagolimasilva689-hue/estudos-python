pessoa = {
    'nome' : 'Ana vellutini Bettencourt ',
    'estado': 'Rio grande do sul',
    'Pais': 'Brasil',
    'Cidade':'Pelotas',
    'Idade':20,
    'Ano nascimento': 2006
}
while True:
   pergunta = input("pergunta a chave: ")
   if pergunta == 'Fim':
       break
   if pergunta in pessoa:
    print("Existem")   
   else:
      print("Não existem")
    
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


produtos ={
    'playstation 5': 4599,
    ' Drone H21':2988,
    'Celular Poco': 4000,
    'Fone de ouvido sem fio': 143.58,
     'Celular iphone 17 pro': 18500,
}
def maior_elemento(produtos):
    maior_preco =max (produtos.values())
    for nome,preco in produtos.items():
        if preco == maior_preco:
           return nome, preco
loja = maior_elemento(produtos)
print(loja)
        

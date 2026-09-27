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
    


        
   





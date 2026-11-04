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
        
        

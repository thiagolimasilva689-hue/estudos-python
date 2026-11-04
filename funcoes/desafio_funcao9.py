def analisar_lista(lista):
    media = sum(lista) / len(lista)
    
    acima = []
    for num in lista:
        if num > media:
            acima.append(num)
    
    quantidade = len(acima)
    
    return media, quantidade, acima


lista = [4,7,8,6,4,5,9,7,8,6]

media, qtd, lista_acima = analisar_lista(lista)

print("Média:", media)
print("Quantidade acima da média:", qtd)
print("Números acima da média:", lista_acima)
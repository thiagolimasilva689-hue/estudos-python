def resultados():
    lista = []
    while True:
        num = int(input("Informe um número: "))
        if num == 0:
             break
        lista.append(num)
    somar = sum(lista)
    quantidade = len(lista)
    if quantidade> 0:
            media = somar / quantidade
    else:
        media = 0
    return somar,quantidade,media
minha_conta = resultados()
print(minha_conta)
 
       

    

def calcular():
    lista = []
    while True:
         num = int(input("Informe um número: "))
         if num == 0:
               break
         lista.append(num)
    somar = sum(lista)
    quantidade = len(lista)
    if quantidade>0:
            media = somar / quantidade
    else:
        media = 0
    return somar,quantidade,media

resultado = calcular()
print("Soma: ",resultado[0])
print("Quantidade: ",resultado[1])
print("Média: ",resultado[2])

    





    
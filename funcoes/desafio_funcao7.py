def pares(lista):
    nova_lista = []
    for num in lista:
        if num % 2 == 0:
            nova_lista.append(num)
    return nova_lista
lista = [2,5,8,7,6,12,48,14,10,22,8]
resultado = pares(lista)
print(resultado)




    
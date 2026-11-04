def somar_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total
lista = [10,20,30,40,50]
resultado = somar_lista(lista)
print("Soma: ",resultado)

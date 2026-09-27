def somar_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total
lista = [10,20,30,40,50]
resultado = somar_lista(lista)
print("Soma: ",resultado)

"""for _ in range(5):
    num = int(input("Informe um número: "))
lista.append(num)
resultado = somar_lista(lista)
print("Lista: ",lista)
print("Total: ",resultado)
"""
def maiores_elementos(lista):
    maiores = []
    for i in lista:
        if i > 10:
            maiores.append(i)
    return maiores
lista = []
while True:
    num = int(input("Informe um numero: "))
    if num == 0:
        break
    lista.append(num)
resultado = maiores_elementos(lista)
print(resultado)
    
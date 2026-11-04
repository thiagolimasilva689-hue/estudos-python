lista = []
while True:
    num =  int(input("Digitei um número: "))
    if num == -1:
        break
    lista.append(num)
quantidade  = len(lista)
somar =  sum(lista)
print('Quantidade é :',quantidade)
print('Somar é :',somar)



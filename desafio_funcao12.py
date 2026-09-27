def mediada(lista):
    maior = max(lista)
    menor=  min(lista)
    return maior,menor
       
lista = []
while True:
    num = int(input("Informe um número: "))
    if num == 0:
        break
    lista.append(num)
mediado_lista = mediada(lista)
print(mediado_lista)

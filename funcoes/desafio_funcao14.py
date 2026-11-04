def maior_media(lista):
    for i in lista:
     media  = sum(lista) / len(lista)
     maiores = []
     for i in lista:
        if i > media:
         maiores.append(i)
     return maiores
   
lista = []
while True:
    num = int(input("Informe um número: "))
    if num == 0:
        break
    lista.append(num)
mediado_lista = maior_media(lista)
print("Números maiores que a media: ",mediado_lista)

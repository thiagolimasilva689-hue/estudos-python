lista = [7,4,8,4,8,9,10]
def verificar_maior(i):
        return max(i)
maior_elemento = verificar_maior(lista)
print("O maior elemento da lista: ",maior_elemento)

def pares(lista):
    nova_lista = []
    for num in lista:
        if num % 2 == 0:
            nova_lista.append(num)
    return nova_lista
lista = [2,5,8,7,6,12,48,14,10,22,8]
resultado = pares(lista)
print(resultado)
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

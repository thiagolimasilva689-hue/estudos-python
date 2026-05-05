lista = []

for i in range(0,5):
    numero = int(input("Informe um numero: "))
    lista.append(numero)
    maior =  max(lista)
    menor =  min(lista)
    media = sum(lista) / len(lista)
print(lista)
print(maior)
print(menor)
print(media)

numeros = [5, 12, 7, 20, 3, 15]
lista = []
for i in numeros:
    if i>10:
        lista.append(i)
print(lista)

lista = []
somar = 0
for i in range(0,5):
    numero = int(input("Informe um numero: "))
    lista.append(numero)
    somar+=numero
print(lista)
print(somar)


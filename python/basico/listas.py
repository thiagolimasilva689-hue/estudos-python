lista = []
somar = 0
for i in range(0,5):
    numero = int(input("Informe um numero: "))
    lista.append(numero)
    somar+=numero
print(lista)
print(somar)

lista = []
while True:
    numero = int(input("Informe um numero: "))
    if numero == 0:
              break
    lista.append(numero)
print(lista)

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

  

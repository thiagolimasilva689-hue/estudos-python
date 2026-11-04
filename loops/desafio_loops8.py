lista = []
pares = []
while True:
    num = int(input("Digitei a número: "))
    if num == 0:
        break
    lista.append(num)

for i in lista:
    if i % 2 == 0:
        pares.append(i)
print(pares)  
 
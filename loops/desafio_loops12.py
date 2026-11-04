def definir():
    numeros = []
    pares = 0
    impar = 0
    for i in range(0,10):
         num = int(input("Informe um numero: "))
         numeros.append(num)
    maior_elemento = max(numeros)
    menor_elemento = min(numeros)
    media = sum(numeros) / len(numeros)
    for i in numeros:
         if i % 2 ==0:
              pares+=1
         else:
              impar+=1
    return maior_elemento,menor_elemento,media,pares,impar
definido = definir()
print("Maior:", definido[0])
print("Menor:", definido[1])
print("Média:", definido[2])
print("Pares:", definido[3])
print("Ímpares:", definido[4])
        

        
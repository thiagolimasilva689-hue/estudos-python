lista = []
for num in range(0,5):
    num = int(input("Digitei um numero: "))
    lista.append(num)

def definidor(lista):
        somar = sum(lista)
        media  = sum(lista) / len(lista)
        return somar,media
resultado =  definidor(lista)
print(lista)
print('Somar: ',resultado[0])
print('Media: ',resultado[1])

 


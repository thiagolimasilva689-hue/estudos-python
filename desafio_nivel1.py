def somar(lista):
        if len(lista)==0:
             return 0,0
        total = sum(lista)
        media = sum(lista) / len(lista)
        return total,media
lista = []
while True:
    num = int(input("Informe um numero: "))
    if num == 0:
        break
    lista.append(num)
resultado = somar(lista)
print(f"A Somar é {resultado[0]}")
print(f"A Media é {resultado[1]}")


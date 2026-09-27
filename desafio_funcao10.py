def analisar_listas(lista):
    maior = max(lista)
    menor = min(lista)
    somar = sum(lista)
    return maior,menor,somar
lista = [10,5,25,74,4,8,4,7]
resultado = analisar_listas(lista)
print(resultado)
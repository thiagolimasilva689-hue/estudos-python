
def maior_10(lista):
    total = 0
    for num in lista:
        if num > 10:
            total+=1
    return total
lista = [12,6,8,6,4,36,5,7]
maiores_elemen = maior_10(lista)
print(maiores_elemen)

def maior_numero():
    lista = []
    while True:
        num = int(input("Informe um número: "))
        if num == 0:
            break
        lista.append(num)
    if len(lista) == 0:
        return "Nenhum número informado"
    maior_elemento = max(lista)
    return maior_elemento
identicar = maior_numero()
print(identicar)
        

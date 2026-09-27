def contar_par():
    par = 0
    while True:
        num = int(input("Informe um número: "))
        if num ==0:
            break
        if num % 2 == 0:
            par+=1
    return par   
identificar = contar_par()
print(identificar)


def contar(frase):
    contador  = 0
    for lentra in frase:
        if lentra == 'a':
            contador+=1
        return contador
frase = input("Informe uma frase: ")
resultado = contar(frase)
print("Quantidade de 'a': ",resultado)
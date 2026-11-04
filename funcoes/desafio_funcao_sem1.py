def somar():
    somartotal = 0
    while True:
       num = int(input("Informe um número: "))
       if num == 0:
         break
       somartotal += num
    return somartotal 
resultado = somar()
print(resultado)

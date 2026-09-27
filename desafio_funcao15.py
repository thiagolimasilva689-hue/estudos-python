def defi_numero(lista):
    par = []
    impar = []
    for i in lista: 
      if i % 2 == 0:
         par.append(i)
      else:
        impar.append(i)
    return par, impar
lista = []
while True:
    num = int(input("Informe um número: "))
    if num == 0:
        break
    lista.append(num)

identi_numero = defi_numero(lista)
print(identi_numero)
    
    
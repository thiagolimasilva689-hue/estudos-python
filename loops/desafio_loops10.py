def contar(num_inicio,num_final):
    for i in range(num_inicio,num_final+1):
          print(i)
num_primeiro = int(input("Informe o primeiro número: "))
num_final = int(input("Informe o ultimo número: "))
contador = contar(num_primeiro,num_final)
print(contador)

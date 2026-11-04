"""


python
# Saída: 10 9 8 7 6 5 4 3 2 1


python
# Saída: 5050

"""

"""
Exercício 1 — Números pares
Use range() para imprimir todos os números pares de 0 a 20.

python
# Saída: 0 2 4 6 8 10 12 14 16 18 20

for num in range(0,21):
    if num % 2 == 0:
        print(num)
"""

"""
Exercício 2 — Contagem regressiva
Use range() para imprimir uma contagem regressiva de 10 até 1.
"""
#for num in range(10,0,-1):
 #   print(num)


"""
Exercício 3 — Soma dos números
Use range() e um acumulador para somar todos os números de 1 a 100. Depois mostre o resultado.
"""
#somar = 0
#for  num in range(1,101):
 #   somar += num
#print(somar)

"""
Exercício 4 — Tabuada
Peça um número ao usuário. Use range() para mostrar a tabuada desse número de 1 a 10.

python
# Digite um número: 7
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
"""
valor = int(input("INFORME A TABUADA:"))
for num in range(0,11):
    print(f"{valor} x {num} = {num * valor}")
 
    
    
    

      

     
  
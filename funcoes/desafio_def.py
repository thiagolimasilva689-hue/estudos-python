"""
Exercício 1 — Maior de dois
Crie uma função maior(a, b) que recebe dois números e retorna o maior.

python
print(maior(5, 9))   # 9
print(maior(10, 3))  # 10

Exercício 2 — Par ou ímpar
Crie uma função par_ou_impar(numero) que retorna "Par" ou "Ímpar".

python
print(par_ou_impar(7))   # Ímpar
print(par_ou_impar(10))  # Par

Exercício 3 — Total com desconto
Crie uma função total_com_desconto(valor, desconto) que recebe um valor e um percentual de desconto, e retorna o valor final.

python
print(total_com_desconto(100, 10))  # 90.0
print(total_com_desconto(200, 25))  # 150.0

Exercício 4 — Filtrar maiores que
Crie uma função filtrar_maiores(lista, limite) que retorna uma nova lista apenas com os números maiores que o limite.

python
print(filtrar_maiores([3, 7, 2, 9, 5], 4))  # [7, 9, 5]

Exercício 5 — Classificar temperatura
Crie uma função classificar_temp(celsius) que retorna:

"Frio" se temperatura < 15

"Agradável" se entre 15 e 30

"Calor" se > 30

python
print(classificar_temp(10))   # Frio
print(classificar_temp(22))   # Agradável
print(classificar_temp(35))   # Calor
"""

#1
def maior(a,b):
    if a> b:
        return a
    else:
        return b
print(maior(5,9))

#2
def classificar_num(num):
       if num % 2 == 0:
         return "Par"
       else:
           return "Ímpar"
print(classificar_num(7))

#3
def total_com_desconto(valor, desconto):
          return valor - (valor * desconto / 100)
print(total_com_desconto(100, 10))

#4
def filtrar_maiores(lista,limite):
     nova_lista = []
     for i in lista:
           if i > limite:
                nova_lista.append(i)
     return nova_lista 
print(filtrar_maiores([3, 7, 2, 9, 5], 4)) 

#5
def classificar_temp(celsius):
     if celsius < 15:
          return "Frio"
     elif celsius <= 30:
         return "Agradável"    
     else:                      
        return "Calor!"
print(classificar_temp(10))

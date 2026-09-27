"""
Exercício 1 (lista + soma + condição)

Peça 6 números ao usuário e guarde em uma lista.

👉 Depois mostre:

a soma total
quantos números são pares
"""
somar = 0
par = 0
lista = []
for i in range(0,6):
      num = int(input("Informe um número: "))
      lista.append(num)
      somar+= num
      if num % 2 == 0:
            par+=1
print("Lista:",lista)
print(f"Soma total é {somar}")
print("Tudos os pares:",par)



  




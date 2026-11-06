
'''
1. Encontrar o maior número
Lista: [12, 5, 27, 9, 18]
Encontre o maior número sem usar max(). Resultado esperado: 27.
'''
Lista= [12, 5, 27, 9, 18]
num_maior = Lista[0]
for num in Lista:
    if num > num_maior:
        num_maior = num
#print(num_maior)

"""
2. Encontrar o menor número
Encontre o menor número sem usar min(). Resultado esperado: -4.
"""
Lista =  [14, 3, 22, -4, 8]
menor_num = Lista[0]
for num in Lista:
    if num < menor_num:
        menor_num =  num
#print(menor_num)


"""
3. Somar e contar números
Lista: 
Calcule a soma e a quantidade de números maiores que 6. Resultado: soma 37, quantidade 4.
"""
Lista = [3, 8, 10, 5, 12, 7]
somar = 0
quantidade = 0
for num in Lista:
    if num > 6:
        somar += num
        quantidade += 1
#print(somar)
#print(quantidade)

'''
4. Contar pares e ímpares
Lista: []
Conte quantos números são pares e quantos são ímpares. Resultado: 4 pares e 3 ímpares.
'''
lista = [2, 7, 10, 13, 16, 21, 24]
impares = 0
pares = 0
for num in lista:
    if num % 2 == 0:
        pares += 1
    else:
        impares +=1
#print(pares)
#print(impares)

"""
5. Média das notas aprovadas
Calcule a média somente das notas maiores ou iguais a 7. Resultado aproximado: 8.17.
"""
lista = [5.5, 8.0, 6.0, 9.5, 7.0, 4.0]
somar = 0
quantidade  = 0
for num in lista:
    if num >= 7:
       somar +=num
       quantidade += 1
media = somar / quantidade
#print(f"A Média é {media:.2f}")


"""
Nível 2 — Listas e raciocínio
Objetivo: aprender a verificar elementos, preservar dados e resolver problemas com várias etapas.

10. Inverter uma lista
Lista: [3, 6, 9, 12, 15]
Crie uma nova lista na ordem inversa sem usar .reverse() nem [::-1].
Resultado: [15, 12, 9, 6, 3].
"""
"""
6. Remover repetições
Lista: [2, 4, 2, 7, 4, 9, 7, 10]
Crie uma nova lista sem elementos repetidos, mantendo a ordem original. Não use set().
Resultado: [2, 4, 7, 9, 10].
"""
valores  = [2, 4, 2, 7, 4, 9, 7, 10]
valores_corrigidos = []
for num in valores:
    if num not in valores_corrigidos:
        valores_corrigidos.append(num)
#print(valores_corrigidos)

"""
7. Contar ocorrências
Conte quantas vezes o número 4 aparece, sem usar .count().
"""
numeros =  [4, 2, 4, 7, 4, 9, 2, 4]
contar = 0
for num in numeros:
    if num == 4:
        contar += 1
#print(contar)

"""
8. Separar números
Lista: 
Crie três listas: positivos, negativos e zeros.
"""
tipos_num =[-3, 0, 8, -1, 5, 0, -7, 2]
positivos =[]
negativos = []
zeros = []
for num in tipos_num:
    if num > 0:
        positivos.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        negativos.append(num)
#print(positivos)
#print(negativos)
#print(zeros)



"""
10. Inverter uma lista
Lista: [3, 6, 9, 12, 15]
Crie uma nova lista na ordem inversa sem usar .reverse() nem [::-1].
Resultado: [15, 12, 9, 6, 3].
"""


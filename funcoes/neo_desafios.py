
"""

Questão 1 — Soma de pares
Crie uma função chamada soma_pares que recebe uma lista de números inteiros e retorna a soma de todos os números pares.

Exemplo:

python
soma_pares([1, 2, 3, 4, 5, 6])
Resultado esperado:


def soma_pares(lista):
    somar = 0
    for i in lista:
        if i % 2 == 0:
            somar += i
    return somar
lista = []
while True:
          num = int(input("INFORME O NÚMERO: "))
          if num == -1:
                break
          lista.append(num)

resultado = soma_pares(lista)
print(f"O RESULTADO FINAL FOI : {resultado}")
"""





"""

Questão 2 — Contar vogais
Crie uma função chamada contar_vogais que recebe uma string e retorna quantas vogais (a, e, i, o, u) existem nela.

Exemplo:

python
contar_vogais("Thiago")
Resultado esperado:

def Contar_vogais(frase):
    contar = 0
    for letra in frase:
            if letra.lower() in "aeiou":
                  contar += 1
    return contar
palavra = input("FALAR QUALQUER COISA AÍ :")
resulta = Contar_vogais(palavra)
print(f"QUANTAS VOGAIS TINHA : {resulta}")

"""


"""
Questão 3 — Maior elemento
Crie uma função chamada maior_elemento que recebe uma lista de números e retorna o maior valor.
Exemplo:
python
maior_elemento([3, 7, 1, 12, 9])

def maior_elemento(lista):
        maior = max(lista)
        return maior        
lista = []
while True:
            num = int(input("INFORME O NÚMERO: "))
            if num == -1:
                      break 
            lista.append(num)             
resultado = maior_elemento(lista)
print(f"O MAIOR ELEMENTO DE TUDOS É {resultado}")
Resultado esperado:
"""

"""
Questão 4 — Filtrar maiores que 10
Crie uma função chamada filtrar_maiores_10 que recebe uma lista de números e retorna uma nova lista apenas com os números maiores que 10.

Exemplo:

python
filtrar_maiores_10([5, 11, 2, 20, 8, 15])
Resultado esperado:

def filtrar_maiores_10(lista):
    nova_lista = []
    for i in lista:
        if i >=10:
            nova_lista.append(i)
    return nova_lista
lista = []
while True:
            num = int(input("INFORME O NÚMERO: "))
            if num == -1:
                  break      
            lista.append(num)    
print(filtrar_maiores_10(lista)) 
"""


"""
Questão 5 — Contar letras de palavras
Crie uma função chamada tamanho_palavras que recebe uma lista de palavras e retorna uma nova lista com a quantidade de letras de cada palavra.
Exemplo:
python
tamanho_palavras(["dados", "python", "sql"])
Resultado esperado:
python
[5, 6, 3]
Se quiser, depois me manda suas respostas que eu corrijo e explico uma por uma. E se quiser questões de SQL também, é só pedir!
"""
def contar_lentrar(lista):
    for i in lista:
        contar = len(i)
    return contar
lista = []
while True:
    frase = input("FALAR QUALQUER COISA AÍ :")
    if frase == 'kkk':
        break
    lista.append(frase)
print(contar_lentrar(lista))









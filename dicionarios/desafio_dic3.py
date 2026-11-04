"""
Exercício 3 — Contar ocorrências 

Crie uma função que recebe uma lista de palavras e retorna um dicionário com cada palavra e quantas vezes ela aparece. 

python 

print(contar(["gato", "cachorro", "gato", "pato", "gato"])) 
# {'gato': 3, 'cachorro': 1, 'pato': 1} 
"""
def contar(lista):
    dic = {}
    for palavra in lista:
        if palavra in dic:         
            dic[palavra] += 1       
        else:
            dic[palavra] = 1        
    return dic
print(contar(["gato", "cachorro", "gato", "pato", "gato"])) 



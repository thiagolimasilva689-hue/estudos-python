"""
Vamos revisar dicionários do seu jeito (simples e direto)
O que é um dicionário
Uma lista onde cada item tem um nome (chave) e um valor.

python
# Lista: acessa por posição (0, 1, 2)
lista = ["Thiago", 20, "Coxim"]

# Dicionário: acessa por nome
pessoa = {
    "nome": "Thiago",
    "idade": 20,
    "cidade": "Coxim"
}


Como usar
python
pessoa["nome"]        # "Thiago"
pessoa["idade"]       # 20
Como adicionar algo novo
python
pessoa["altura"] = 1.75
Como verificar se existe
python
if "nome" in pessoa:
    print("Existe")

    Como percorrer
python
for chave, valor in pessoa.items():
    print(chave, valor)
Tenta o desafio 1 de novo com essa base
python
def conta(frase):
    dicio = {}
    palavras = frase.split()
    for palavra in palavras:
        if palavra in dicio:
            dicio[palavra] = dicio[palavra] + 1
        else:
            dicio[palavra] = 1
    return dicio



"""
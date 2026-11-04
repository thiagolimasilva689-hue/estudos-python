produtos = []

while True:
    itens = input("Informe o produto: ")

    if itens == 'fim':
        break

    produtos.append(itens)

print("Produtos cadastrados:")

for i in produtos:
    print(i)

print("Quantidade:", len(produtos))

maior_nome = max(produtos, key=len)

print("Maior nome:", maior_nome)


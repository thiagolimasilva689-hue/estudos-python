produtos = {
    'miojo apimentado': 2.89,
    'pizza': 35.89,
    'guaraná': 12.89
}
while True:
    pergunta = input("Pesquise o produto (ou 'Fim' para sair): ").lower()
    
    if pergunta == 'fim':
        print("Até logo!")
        break
    
    if pergunta in produtos:
        print(f"Preço: R$ {produtos[pergunta]:.2f}")
    else:
        print("Produto não encontrado.")
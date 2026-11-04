lista = []
while True:
    usuario = input("Informe o seu nome: ")
    
    if usuario.lower() == 'sair':
        break
    lista.append(usuario)
    print("\n Lista de nomes:")
for nome in lista:
    print(nome)

    
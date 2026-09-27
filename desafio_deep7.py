senha = 'teiu$#9845'
while True:
    digitei = input("Digitei a senha: ")
    if digitei == senha:
        print('Correto,acesso liberado!')
    else:
        print('Senha incorreta, digitei novamente')
    if digitei == 'Fim':
        print("Acabou")
        break
      
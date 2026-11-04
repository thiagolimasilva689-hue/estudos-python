senha = 1234
conta = 0
while True:
    infor = int(input("Informe a senha: "))
    if infor == senha:
        print("Acesso Liberado!")
        break
    else:
        print("Informe novamente!")
    conta+=1

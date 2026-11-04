def vida(idade):
    if idade < 12:
        return('Criança')
    elif idade >= 12 and idade <+ 17:
        return('Adolescente')
    elif idade >= 18 and idade <= 63:
        return('Adulto')
    elif idade > 64:
        return('Idosos')
idade = int(input("Informe a sua idade: "))
classificar = vida(idade)
print(classificar)


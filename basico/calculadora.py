# faça uma calculadora com if,else e elif
print('-'*5,"CALCULADORA DIGITAL",'-'*5)
n1 = float(input("Informe o seu primeiro numero: "))
n2 = float(input("Informe o seu segundo numero: "))
opera_arit = input("informe o seu operador aritmetico:")

if opera_arit == '+':
    print(f"{n1} + {n2} = { n1 + n2}")
elif opera_arit == '-':
    print(f"{n1} - {n2} = { n1 - n2}")
elif opera_arit == '*':
    print(f"{n1} * {n2} = { n1 * n2}")    
elif opera_arit == '/':
    print(f"{n1} / {n2} = { n1 / n2}")   
elif opera_arit == '//':
    print(f"{n1} // {n2} = { n1 // n2}")   
elif opera_arit == '**':
    print(f"{n1} ** {n2} = { n1 ** n2}")   
elif opera_arit == '%':
    print(f"{n1} % {n2} = { n1 % n2}")   

print('-'*15)    

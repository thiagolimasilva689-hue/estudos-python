frase = input("Informe uma frase: ")
conta = 0
for lentra in frase.lower():
    if lentra == 'a':
         conta += 1
    elif lentra == 'e':
              conta += 1
    elif lentra == 'i':
              conta += 1
    elif lentra == 'o':
              conta += 1
    elif lentra == 'u':
              conta += 1
print("Quantidade de vogais:",conta)

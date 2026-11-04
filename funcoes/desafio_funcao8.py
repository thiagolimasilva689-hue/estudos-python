def vogais(lentras):
    contar = 0
    for i in lentras:
        if i in "aeiou":
            contar+=1
    return contar
frases =  vogais(input("Informe uma palavra: "))
print(frases)
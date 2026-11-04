def vogais():
    total_vogal = 0
    while True:
        frase = input("Informe uma frase: ")
        if frase == 'Fim':
            break
        for lentra in frase:
            if lentra.lower() in "aeiou":
                total_vogal +=1
        return total_vogal
palavras = vogais()
print(palavras)
        





        

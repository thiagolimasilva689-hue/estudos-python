soma_idades = 0
contador_maiores = 0

total_pessoas = int(input("Quantas pessoas vamos cadastrar? "))
for i in range(total_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    soma_idades+= idade
    if idade >= 18:
        contador_maiores+=1
print(f"A soma total é: {soma_idades}")
print(f"Pessoas maiores de 18: {contador_maiores}")    

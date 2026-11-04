def conta(frase):
    dicio = {}
    palavras = frase.split()   # <- isso separa a frase em palavras
    for palavra in palavras:   # <- percorre cada palavra
        if palavra in dicio:
            dicio[palavra] = dicio[palavra] + 1
        else:
            dicio[palavra] = 1
    return dicio




   
   
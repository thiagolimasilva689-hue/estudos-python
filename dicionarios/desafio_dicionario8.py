gastos_semana ={
    'Porter de sorvede de um 1 lintro' : 55.8,
    'Lanche':33.8,
    '9 macarrão apimentado': 25,
    'pizza artensal': 45.89,
    'Credito do celular':20
}
def somar_gastos(gastos_semana):
    total_gastos = sum(gastos_semana.values())
    return total_gastos
total = somar_gastos(gastos_semana)
print(total)

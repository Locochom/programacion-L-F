def  preparar_hotkakes():
    return "🥞"

def ordenar_hotkakes(numero_piezas):
    hotkakes = [preparar_hotkakes() for _ in range(numero_piezas)]
    return hotkakes

familia = ordenar_hotkakes(int(input('Ingresa tu orden:')))
print(familia)
def  preparar_hotdog():
    return "🌭"

def  preparar_hamburguesa():
    return "🍔"

def  preparar_pizza():
    return "🍕"

def calcular_bonus(num_ordenes):
    if (num_ordenes > 2):
        return "🥤 gratis"
    else:
        return ""

def ordenar_alimento(preparar_orden, num_ordenes):
    pedido = [preparar_orden() for _ in range(num_ordenes)]
    bonus = calcular_bonus(num_ordenes)
    return num_ordenes, bonus

orden_grupo_a = ordenar_alimento(preparar_hotdog,int(input("Ingrese su orden:")))
print(orden_grupo_a)

orden_grupo_b = ordenar_alimento(preparar_hamburguesa,int(input("Ingrese su orden:")))
print(orden_grupo_b)

orden_grupo_c = ordenar_alimento(preparar_pizza,int(input("Ingrese su orden:")))
print(orden_grupo_c)


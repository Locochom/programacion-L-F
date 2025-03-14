def preparar_cafe_americano():
    return "café americano"

def preparar_cafe_olla():
    return "cafe de olla"

def ordenar_cafe(preparar_cafe, num_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(num_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(preparar_cafe_olla,int(input("Ingrese su orden:")))
print(cafe_grupo_a)

cafe_grupo_b = ordenar_cafe(preparar_cafe_americano,int(input("Ingrese su orden:")))
print(cafe_grupo_b)
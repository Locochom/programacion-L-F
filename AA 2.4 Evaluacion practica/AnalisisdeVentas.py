from functools import reduce


ventas_pesos = [1500, 2500, 3200, 4500, 6000, 1200, 8000]
tipo_cambio = 20.46 
umbral_dolares = 150


promedio_pesos = reduce(lambda acumulado, venta: acumulado + venta, ventas_pesos) / len(ventas_pesos)


ventas_dolares = list(map(lambda venta: round(venta / tipo_cambio, 2), ventas_pesos))


ventas_filtradas = list(filter(lambda venta: venta > umbral_dolares, ventas_dolares))


suma_filtradas = reduce(lambda acumulado, venta: acumulado + venta, ventas_filtradas, 0)


print(f"Promedio de ventas en pesos mexicanos: {promedio_pesos:.2f} MXN")
print(f"Ventas en dólares: {ventas_dolares}")
print(f"Ventas mayores a {umbral_dolares} USD: {ventas_filtradas}")
print(f"Suma total de ventas mayores a {umbral_dolares} USD: {suma_filtradas:.2f} USD")

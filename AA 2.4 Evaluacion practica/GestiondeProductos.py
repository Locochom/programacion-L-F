productos = ["Frijoles Refritos", "Coca Cola", "Zumo de Naranja", "Café de Olla", "Gorditas de Chicharron", "Huevos Motuleños"]

productos_ordenados = sorted(productos)
cadena_productos= ", ".join(productos_ordenados)
productos_slug = list(map(lambda nombre: nombre.lower().replace(" ","-"), productos_ordenados))

print("Lista de slugs:",productos_slug)
print("Cadena de Nombres Ordenados:",cadena_productos)
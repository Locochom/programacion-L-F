def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma(a, b):
    return(a + b)

def resta(a, b):
    return(a - b)


resultado = operar(5, 3, suma)
print(resultado)

def saludo():
    return "Hola"

mi_variable = saludo()
print(mi_variable)

def saludo2():
    return "Que tal"

mi_variable2 = saludo2()
print(mi_variable2)

def elegir_operacion(operacion):
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2
    if operacion == "multiplicar":
        return multiplicar
    else:
        return dividir
    
doble = elegir_operacion("multiplicar")
print(doble(10))
divide2 = elegir_operacion("dividir")
print(divide2(10))    


doble = lambda x: x * 2
print(doble(5))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

alumnos = ['Alejandro', 'Miguel', 'Vinicio', 'Rodney','Marcial']
saludar_alumnos = list(map(lambda nombre:   'Hola' + nombre, alumnos))
#print(saludar_alumnos)

#sin lambda
def saludar(nombre):
    return 'Hola' + nombre
#usamos map con la funcion saludar
lista_saludos = list(map(saludar, alumnos))
print(lista_saludos)


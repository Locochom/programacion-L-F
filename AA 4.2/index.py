from functools import reduce

# Datos de las zonas y sensores
zonas = ['norte', 'sur', 'este', 'oeste']

humedad_suelo = {
    'norte': 'baja',
    'sur': 'media',
    'este': 'alta',
    'oeste': 'baja'
}

temperatura = {
    'norte': 35,
    'sur': 29,
    'este': 32,
    'oeste': 33
}

hora = {
    'norte': 20,
    'sur': 15,
    'este': 8,
    'oeste': 21
}

pronostico_lluvia = {
    'norte': False,
    'sur': True,
    'este': False,
    'oeste': False
}

# Verificar si la hora es adecuada
hora_adecuada = lambda zona: hora[zona] < 10 or hora[zona] > 18

# Condiciones para activar riego
activar_riego = lambda zona: humedad_suelo[zona] == 'baja' and not pronostico_lluvia[zona] and hora_adecuada(zona)

# Estado del riego
estado_riego = lambda zona: 'Activado' if activar_riego(zona) else 'No activado'

# Alerta por temperatura
alerta_calor = lambda zona: temperatura[zona] >= 32

# Recomendaciones
def recomendacion(zona):
    if activar_riego(zona) and alerta_calor(zona):
        return f"Zona {zona}: Alerta: riego activado con temperatura alta. Considere riego nocturno o por goteo."
    elif activar_riego(zona):
        return f"Zona {zona}: Sin recomendaciones especiales para el riego."
    else:
        return f"Zona {zona}: Sin recomendaciones especiales para el riego."

# Diagnóstico total
def diagnostico_total():
    list(map(lambda z: print(f"Zona {z}: Riego {estado_riego(z)}\n{recomendacion(z)}"), zonas))

# Ejecutar diagnóstico
diagnostico_total()

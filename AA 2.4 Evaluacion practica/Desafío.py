import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Asignación de Materias")

# Crear los widgets para las calificaciones de cada materia
label_instrucciones = tk.Label(root, text="Califica cada aspecto de las materias (1-5):")
label_instrucciones.grid(row=0, column=0, columnspan=4)

# Programación Lógica y Funcional
label_programacion = tk.Label(root, text="Programación Lógica y Funcional")
label_programacion.grid(row=1, column=0, columnspan=4)

label_actividades_programacion = tk.Label(root, text="Actividades:")
label_actividades_programacion.grid(row=2, column=0)
entry_actividades_programacion = tk.Entry(root)
entry_actividades_programacion.grid(row=2, column=1)

label_herramientas_programacion = tk.Label(root, text="Herramientas:")
label_herramientas_programacion.grid(row=3, column=0)
entry_herramientas_programacion = tk.Entry(root)
entry_herramientas_programacion.grid(row=3, column=1)

label_contenido_programacion = tk.Label(root, text="Contenido:")
label_contenido_programacion.grid(row=4, column=0)
entry_contenido_programacion = tk.Entry(root)
entry_contenido_programacion.grid(row=4, column=1)

label_evaluacion_programacion = tk.Label(root, text="Evaluación:")
label_evaluacion_programacion.grid(row=5, column=0)
entry_evaluacion_programacion = tk.Entry(root)
entry_evaluacion_programacion.grid(row=5, column=1)

# Administración de Redes
label_redes = tk.Label(root, text="Administración de Redes")
label_redes.grid(row=6, column=0, columnspan=4)

label_actividades_redes = tk.Label(root, text="Actividades:")
label_actividades_redes.grid(row=7, column=0)
entry_actividades_redes = tk.Entry(root)
entry_actividades_redes.grid(row=7, column=1)

label_herramientas_redes = tk.Label(root, text="Herramientas:")
label_herramientas_redes.grid(row=8, column=0)
entry_herramientas_redes = tk.Entry(root)
entry_herramientas_redes.grid(row=8, column=1)

label_contenido_redes = tk.Label(root, text="Contenido:")
label_contenido_redes.grid(row=9, column=0)
entry_contenido_redes = tk.Entry(root)
entry_contenido_redes.grid(row=9, column=1)

label_evaluacion_redes = tk.Label(root, text="Evaluación:")
label_evaluacion_redes.grid(row=10, column=0)
entry_evaluacion_redes = tk.Entry(root)
entry_evaluacion_redes.grid(row=10, column=1)

# Inteligencia Artificial
label_ia = tk.Label(root, text="Inteligencia Artificial")
label_ia.grid(row=11, column=0, columnspan=4)

label_actividades_ia = tk.Label(root, text="Actividades:")
label_actividades_ia.grid(row=12, column=0)
entry_actividades_ia = tk.Entry(root)
entry_actividades_ia.grid(row=12, column=1)

label_herramientas_ia = tk.Label(root, text="Herramientas:")
label_herramientas_ia.grid(row=13, column=0)
entry_herramientas_ia = tk.Entry(root)
entry_herramientas_ia.grid(row=13, column=1)

label_contenido_ia = tk.Label(root, text="Contenido:")
label_contenido_ia.grid(row=14, column=0)
entry_contenido_ia = tk.Entry(root)
entry_contenido_ia.grid(row=14, column=1)

label_evaluacion_ia = tk.Label(root, text="Evaluación:")
label_evaluacion_ia.grid(row=15, column=0)
entry_evaluacion_ia = tk.Entry(root)
entry_evaluacion_ia.grid(row=15, column=1)

# Botón para calcular los resultados sin usar funciones ni bucles
button_calcular = tk.Button(root, text="Calcular Resultados", command=lambda: [
    # Obtener las calificaciones ingresadas por el usuario
    entry_actividades_programacion.get(),
    entry_herramientas_programacion.get(),
    entry_contenido_programacion.get(),
    entry_evaluacion_programacion.get(),
    entry_actividades_redes.get(),
    entry_herramientas_redes.get(),
    entry_contenido_redes.get(),
    entry_evaluacion_redes.get(),
    entry_actividades_ia.get(),
    entry_herramientas_ia.get(),
    entry_contenido_ia.get(),
    entry_evaluacion_ia.get(),

    # Obtener y convertir en enteros los valores de las entradas
    actividades_programacion := int(entry_actividades_programacion.get()),
    herramientas_programacion := int(entry_herramientas_programacion.get()),
    contenido_programacion := int(entry_contenido_programacion.get()),
    evaluacion_programacion := int(entry_evaluacion_programacion.get()),

    actividades_redes := int(entry_actividades_redes.get()),
    herramientas_redes := int(entry_herramientas_redes.get()),
    contenido_redes := int(entry_contenido_redes.get()),
    evaluacion_redes := int(entry_evaluacion_redes.get()),

    actividades_ia := int(entry_actividades_ia.get()),
    herramientas_ia := int(entry_herramientas_ia.get()),
    contenido_ia := int(entry_contenido_ia.get()),
    evaluacion_ia := int(entry_evaluacion_ia.get()),

    # Sumar las calificaciones de cada aspecto para cada materia
    programacion_logica_y_funcional := actividades_programacion + herramientas_programacion + contenido_programacion + evaluacion_programacion,
    administracion_de_redes := actividades_redes + herramientas_redes + contenido_redes + evaluacion_redes,
    inteligencia_artificial := actividades_ia + herramientas_ia + contenido_ia + evaluacion_ia,

    # Calcular los promedios
    promedio_programacion_logica_y_funcional := programacion_logica_y_funcional / 4,
    promedio_administracion_de_redes := administracion_de_redes / 4,
    promedio_inteligencia_artificial := inteligencia_artificial / 4,

    # Calcular el promedio general
    promedio_general := (programacion_logica_y_funcional + administracion_de_redes + inteligencia_artificial) / 3,

    # Mostrar los resultados en la GUI
    label_resultados.config(
        text=f"Programación Lógica y Funcional: {programacion_logica_y_funcional} | Promedio: {promedio_programacion_logica_y_funcional}\n"
             f"Administración de Redes: {administracion_de_redes} | Promedio: {promedio_administracion_de_redes}\n"
             f"Inteligencia Artificial: {inteligencia_artificial} | Promedio: {promedio_inteligencia_artificial}\n"
             f"Promedio General: {promedio_general}"
    )
])

button_calcular.grid(row=16, column=0, columnspan=4)

# Label para mostrar los resultados
label_resultados = tk.Label(root, text="", justify="left")
label_resultados.grid(row=17, column=0, columnspan=4)

# Iniciar la GUI
root.mainloop()

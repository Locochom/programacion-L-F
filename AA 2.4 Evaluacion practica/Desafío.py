import tkinter as tk

root = tk.Tk()
root.title("Evaluación de Materias - Alumnos")

materias = ["Programación", "Redes", "Inteligencia Artificial"]
aspectos = ["Actividades", "Herramientas", "Contenido", "Evaluación"]
num_alumnos = 4

entradas = []
nombres = []

# Encabezado
tk.Label(root, text="Evaluación de 3 materias por 4 alumnos", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=20, pady=10)

# Entradas para nombres de alumnos
for i in range(num_alumnos):
    tk.Label(root, text=f"Nombre del Alumno {i+1}:").grid(row=1, column=i*5, columnspan=2)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=2, column=i*5, columnspan=2)
    nombres.append(entry_nombre)

# Generar campos de evaluación
fila = 3
for m in materias:
    tk.Label(root, text=m, font=("Arial", 10, "bold")).grid(row=fila, column=0, sticky='w', pady=(10, 0))
    fila += 1
    for asp in aspectos:
        tk.Label(root, text=asp).grid(row=fila, column=0, sticky='e')
        fila_actual = []
        for i in range(num_alumnos):
            entry = tk.Entry(root, width=5)
            entry.grid(row=fila, column=i+1)
            fila_actual.append(entry)
        entradas.append(fila_actual)
        fila += 1

label_resultados = tk.Label(root, text="", justify="left")
label_resultados.grid(row=fila+2, column=0, columnspan=10, pady=10)

# Botón para calcular
def calcular():
    totales = [0] * num_alumnos
    conteo = [0] * num_alumnos
    todos_los_valores = []

    for grupo in entradas:
        for i in range(num_alumnos):
            try:
                val = int(grupo[i].get())
                totales[i] += val
                conteo[i] += 1
                todos_los_valores.append(val)
            except:
                pass  # Si no es número válido, lo ignora

    resultado = ""
    for i in range(num_alumnos):
        nombre = nombres[i].get() or f"Alumno {i+1}"
        promedio = totales[i] / conteo[i] if conteo[i] > 0 else 0
        resultado += f"{nombre} - Total: {totales[i]} | Promedio: {promedio:.2f}\n"

    total_general = sum(totales)
    promedio_general = total_general / (sum(conteo) if sum(conteo) > 0 else 1)
    maximo = max(todos_los_valores) if todos_los_valores else 0
    minimo = min(todos_los_valores) if todos_los_valores else 0

    resultado += f"\nTotal General: {total_general}"
    resultado += f"\nPromedio General: {promedio_general:.2f}"
    resultado += f"\nValor Máximo: {maximo}"
    resultado += f"\nValor Mínimo: {minimo}"

    label_resultados.config(text=resultado)

boton = tk.Button(root, text="Calcular Resultados", command=calcular)
boton.grid(row=fila+1, column=0, columnspan=10, pady=10)

root.mainloop()

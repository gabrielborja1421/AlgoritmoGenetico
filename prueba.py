import tkinter as tk
from tkinter import ttk
import pandas as pd

# Datos de ejemplo
datos = [
    ["Alimento 1", "Categoría 1", 100, 10, 5, 20, 2, 1000, 0.5, 0.8, 5, 50, 80, "Resultado 1", "Deseado 1"],
    ["Alimento 2", "Categoría 2", 200, 15, 8, 30, 3, 1500, 0.7, 1.2, 8, 70, 100, "Resultado 2", "Deseado 2"],
    ["Alimento 3", "Categoría 1", 150, 12, 6, 25, 2.5, 1200, 0.6, 1.0, 6, 60, 90, "Resultado 3", "Deseado 3"],
    # Agrega más filas según sea necesario
]

columnas = ["Alimento", "Categoría", "Energía", "Proteína", "Grasa", "Calcio", "Hierro", "Vitamina_A", "Tiamina", "Riboflavina", "Niacina", "Folato", "Vitamina_C", "Resultado", "Deseado"]

# Crear una ventana
ventana = tk.Tk()
ventana.title("Tabla de Alimentos")

# Crear el Treeview
tree = ttk.Treeview(ventana)
tree["columns"] = columnas
tree["show"] = "headings"

# Configurar las columnas
for col in columnas:
    tree.column(col, width=80)  # Ajustar el ancho de las columnas aquí

# Configurar el encabezado
for col in columnas:
    tree.heading(col, text=col)

# Agregar los datos a la tabla
for fila in datos:
    tree.insert("", "end", values=fila)

# Agregar el Treeview a la ventana
tree.pack()

# Iniciar el bucle de eventos
ventana.mainloop()

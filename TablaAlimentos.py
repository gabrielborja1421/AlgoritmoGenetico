import tkinter as tk
import tkinter.ttk as ttk

class TablaAlimentos:
    def __init__(self, datos):
        self.datos = datos
        self.ventana = tk.Tk()
        self.ventana.title("Tabla de Alimentos")

        self.tabla = ttk.Treeview(self.ventana)
        self.tabla["columns"] = ("Nombre", "Categoría", "Energía", "Proteína", "Grasa", "Calcio", "Hierro", "Vitamina A", "Tiamina", "Riboflavina", "Niacina", "Folato", "Vitamina C")
        self.tabla.grid(row=0, column=0)

        # Ajustar el ancho de las columnas
        self.tabla.column("#0", width=0)  # Columna de índices
        for columna in self.tabla["columns"]:
            self.tabla.column(columna, width=100)  # Ajustar el ancho de las columnas de datos

        for columna in self.tabla["columns"]:
            self.tabla.heading(columna, text=columna)

        for i, dato in enumerate(self.datos, start=1):
            self.tabla.insert("", "end", text=str(i), values=(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7], dato[8], dato[9], dato[10], dato[11], dato[12]))

    def mostrar(self):
        self.ventana.mainloop()
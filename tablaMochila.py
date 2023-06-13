import tkinter as tk
from tkinter import ttk

class tablaPesos:
    def create_table(self, weights, new_weights, data_YC, data_X, data_YD):
        # Crear ventana principal
        root = tk.Tk()
        root.title("Tabla con Tkinter")

        # Crear Treeview
        tree = ttk.Treeview(root, columns=('X', 'Pesos', 'Nuevos Pesos', 'YD', 'YC'), show='headings')
        tree.grid(row=0, column=0, columnspan=5, padx=10, pady=5)

        # Establecer encabezados
        tree.heading('X', text='X')
        tree.heading('Pesos', text='Pesos')
        tree.heading('Nuevos Pesos', text='Nuevos Pesos')
        tree.heading('YD', text='YD')
        tree.heading('YC', text='YC')

        # Establecer anchos de columna
        tree.column('X', width=220)
        tree.column('Pesos', width=220)
        tree.column('Nuevos Pesos', width=320)
        tree.column('YD', width=200)
        tree.column('YC', width=200)

        # Llenar la tabla con los datos
        num_rows = max(len(weights), len(new_weights), len(data_YC), len(data_X), len(data_YD))
        for i in range(num_rows):
            row = [
                data_X[i] if i < len(data_X) else '',
                weights[i] if i < len(weights) else '',
                new_weights[i] if i < len(new_weights) else '',
                data_YD[i] if i < len(data_YD) else '',
                data_YC[i] if i < len(data_YC) else ''
            ]
            tree.insert('', 'end', values=row)

        # Ejecutar la ventana
        root.mainloop()

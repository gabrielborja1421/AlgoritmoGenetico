import tkinter as tk
from tkinter import font

""" root.geometry("1000x600")  # Establecer la geometría de la ventana
root.title("Algoritmo genetico")

centralwidget = tk.Frame(root)
centralwidget.pack()

widget_2 = tk.Frame(centralwidget, bg="#F5F190")
widget_2.pack()

widget = tk.Frame(widget_2, bg="white")
widget.place(x=0, y=70, width=982, height=512)
widget.pack()

label = tk.Label(widget, text="Pob_incial", font=("Montserrat", 24), bg="white", fg="#1E1E1E")
label.place(x=150, y=70)

pob_init = tk.Entry(widget, width=50)
pob_init.place(x=330, y=70)

label_2 = tk.Label(widget, text="Pob_max", font=("Montserrat", 24), bg="white", fg="#1E1E1E")
label_2.place(x=150, y=130)

pob_max = tk.Entry(widget, width=50)
pob_max.place(x=330, y=130)

label_3 = tk.Label(widget, text="Prob_Cruza", font=("Montserrat", 24), bg="white", fg="#1E1E1E")
label_3.place(x=140, y=250)

Prob_cruza = tk.Entry(widget, width=20)
Prob_cruza.place(x=120, y=280)

label_4 = tk.Label(widget, text="Prob_mutacion", font=("Montserrat", 24), bg="white", fg="#1E1E1E")
label_4.place(x=360, y=250)

Prob_mutacion = tk.Entry(widget, width=20)
Prob_mutacion.place(x=360, y=280)

label_5 = tk.Label(widget, text="Objetivo", font=("Montserrat", 24), bg="white", fg="#1E1E1E")
label_5.place(x=140, y=380)

Objetivo = tk.Entry(widget, width=20)
Objetivo.place(x=120, y=410)

label_6 = tk.Label(widget, text="Prob_genes", font=("Montserrat", 24), bg="white", fg="#1E1E1E")
label_6.place(x=640, y=250)

Prob_genes = tk.Entry(widget, width=20)
Prob_genes.place(x=620, y=280)

button = tk.Button(widget, text="Button", font=("Arial", 24), bg="#72B960", fg="white")
button.place(x=756, y=438, width=187, height=60)

label_8 = tk.Label(widget, text="tipo", font=("Montserrat", 24), bg="white", fg="#1E1E1E")
label_8.place(x=390, y=380)

enfoque = tk.Entry(widget, width=20)
enfoque.place(x=370, y=410)

label_7 = tk.Label(widget_2, text="Rellene los siguientes campos", font=("Montserrat", 32), bg="white", fg="#1E1E1E")
label_7.place(x=250, y=10, width=491, height=39)

root.mainloop() """

root = tk.Tk()
root.config(bg="#FFFFFF")
centralwidget= tk.Frame(root)
centralwidget.pack()

widget_2 = tk.Frame(root, bg="#F5F190")
widget_2.place(x=0, y=0, width=1000, height=70)

fuente = font.Font(family="Montserrat", size=24, weight="bold")
fuente2 = font.Font(family="Montserrat", size=18, weight="bold")
fuente3 = font.Font(family="Montserrat", size=24, weight="bold")
y1 = 305
y2 = 350
y3 = 440
y4 = 483

label = tk.Label(root, text="Pob_incial", font=fuente2, fg="#1E1E1E", bg="white")
label.place(x=150, y=145)

pob_init = tk.Entry(root, width=30,font=fuente2, bg="#7ce2cc", bd=0, highlightthickness=2, highlightbackground="black")
pob_init.place(x=330, y=150)

label_2 = tk.Label(root, text="Pob_max", font=fuente2, bg="white", fg="#1E1E1E")
label_2.place(x=150, y=200)

pob_max = tk.Entry(root,width=30,font=fuente2, bg="#7ce2cc", bd=0, highlightthickness=2, highlightbackground="black")
pob_max.place(x=330, y=205)

label_3 = tk.Label(root, text="Prob_Cruza", font=fuente2, bg="white", fg="#1E1E1E")
label_3.place(x=135, y=y1)

Prob_cruza = tk.Entry(root, width=10,font=fuente, bg="#7ce2cc", bd=0, highlightthickness=2, highlightbackground="black")
Prob_cruza.place(x=120, y=y2)

label_4 = tk.Label(root, text="Prob_mutacion", font=fuente2, bg="white", fg="#1E1E1E")
label_4.place(x=360, y=y1)

Prob_mutacion = tk.Entry(root, width=10,font=fuente, bg="#7ce2cc", bd=0, highlightthickness=2, highlightbackground="black")
Prob_mutacion.place(x=370, y=y2)

label_6 = tk.Label(root, text="Prob_genes", font=fuente2, bg="white", fg="#1E1E1E")
label_6.place(x=635, y=y1)

Prob_genes = tk.Entry(root, width=10,font=fuente, bg="#7ce2cc", bd=0, highlightthickness=2, highlightbackground="black")
Prob_genes.place(x=620, y=y2)

label_5 = tk.Label(root, text="Objetivo", font=fuente2, bg="white", fg="#1E1E1E")
label_5.place(x=140, y=y3)

Objetivo = tk.Entry(root, width=10,font=fuente, bg="#7ce2cc", bd=0, highlightthickness=2, highlightbackground="black")
Objetivo.place(x=120, y=y4)


label_8 = tk.Label(root, text="Tipo", font=fuente2, bg="white", fg="#1E1E1E")
label_8.place(x=390, y=y3)

enfoque = tk.Entry(root, width=10, font=fuente, bg="#7ce2cc", bd=0, highlightthickness=2, highlightbackground="black")
enfoque.place(x=370, y=y4)

button = tk.Button(root, text="Obtener", font=fuente, bg="#72B960", fg="white")
button.place(x=756, y=508, width=187, height=60)

label_7 = tk.Label(root, text="Rellene los siguientes campos", font=fuente3,  bg="#F5F190", fg="#1E1E1E")
label_7.place(x=150, y=10, width=700, height=50)
root.geometry("1000x600")
root.mainloop() 









""" 
lis = ["lili","juan","jose","luis","josue","Jorge","Ana"]
l = [8,4,2,5,6,6,7,3,3,4]
for x in l:
    print (f'Nombre : {x}')
for x in range(len(lis)):
    print (f'numero de lista : {x}')



def completar_lista(lista):
    repetidos = []
    resultado = []

    for numero in lista:
        if numero not in resultado:
            resultado.append(numero)
        else:
            repetidos.append(numero)

    numeros_faltantes = set(range(1, 115)) - set(resultado)
    numeros_faltantes = sorted(list(numeros_faltantes))

    for numero in repetidos:
        resultado.append(numeros_faltantes.pop(0))

    return resultado
 """
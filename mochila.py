import random
import numpy as np
from Alimentos import *
from PyQt5 import QtWidgets, uic
import tkinter as tk
from tkinter import font
from tablaMochila import *
import matplotlib.pyplot as plt
from TablaAlimentos import TablaAlimentos
class mochila:

    def __init__(self,pob_inicial,pob_max,prob_cruza,prob_mutacion,prob_genes,fitness,objetivo):

        self.pob = pob_inicial
        self.pob_max = pob_max
        self.prob_cruza = prob_cruza
        self.prob_mutacion = prob_mutacion
        self.prob_genes = prob_genes
        self.fitness = fitness
        self.MaxMochila = 3000
        self.objetivo= objetivo

        self.alimentos = []
        self.datos=[]
        df = pd.read_excel("dataset alimentos.xlsx")


        for index, row in df.iterrows():
            alimento = Alimento(row['Alimento'], row['Categoria'], row['Energía'], row['Proteína'], row['Grasa'], row['Calcio'], row['Hierro'], row['Vitamina A'], row['Tiamina'], row['Riboflavina'], row['Niacina'], row['Folato'], row['Vitamina C'])
            self.alimentos.append(alimento)
        

    def generar_individuo (self, cantidad):
        rango = list(range(1,115))
        random.shuffle(rango)
        individuo = rango[:cantidad]
        return individuo

    def crear_pob_inicial (self,poblacion):
        pob = []
        for x in range(poblacion):
            pob.append(self.generar_individuo(114))
        return pob
            

 

    def fitness_pro(self, individuo):
        total = 0
        enfoque = self.fitness
        count = 0
        
        for i in range(len(individuo)):
            count += 1
            numero = individuo[i] - 1
            
            if count < 30:
                total += self.alimentos[numero].__getattribute__(self.fitness)

        return total

    def diferencia(self,individuo):
        diferencia_relativa = abs(self.fitness_pro(individuo) - self.objetivo) / abs(self.objetivo)
        return diferencia_relativa
  



    def seleccion(self,pob):
        fitness = [self.fitness_pro(i) for i in pob]
        fitness_suma = sum(fitness)
        prob = [f / fitness_suma for f in fitness]
        i_padres = np.random.choice(
            len(pob), size=2, replace=False, p=prob)
        return pob[i_padres[0]], pob[i_padres[1]]
        
    def cruza(self,fathers):

        if random.random() < self.prob_cruza:
            longitud = min(len(fathers[0]), len(fathers[1]))
            cruza = random.randint(1, longitud -1)

            hijo1 = fathers[0][:cruza] + fathers[1][cruza:]
            hijo2 = fathers[1][: cruza] + fathers[0] [cruza:]
            """ print(f'\n\nel padre numero 1 es {fathers[0]}\n\n el padre 2 es: {fathers[1]}\n\n')
            print(f'\n\nel hijo numero 1 es {hijo1} \n\n el hijo 2 es {hijo2}') """
            hijo1=self.completar_lista(hijo1)
            hijo2=self.completar_lista(hijo2)
            """ print(f'hijo uno : {hijo1} \n\n hijo dos: {hijo2}') """
            """ print(f'\n\n\nh i j o 1   {hijo1}  \n\n\n')
            print(f'\n\n\nh i j o 2   {hijo2}  \n\n\n') """
            return hijo1, hijo2
        return fathers[0], fathers[1]
       
      
    
    def generaciones(self):
        pob_nueva = self.crear_pob_inicial(self.pob)
        peores_individuos=[]
        mejores_individuos=[]
        medias=[]
        while len(pob_nueva) < self.pob_max:
            padres = self.seleccion(pob_nueva)
            hijo1, hijo2 = self.cruza(padres)

            
            if random.uniform(0, 1) <= self.prob_mutacion:
                """ print(f'\n\neste es el hijo 1\n{hijo1}\n\n') """
                hijo1 = self.mutacion_gen(hijo1)
                """ print(f'\n\neste es el hijo mutado 1\n{hijo1}\n\n') """
            if random.uniform(0, 1) <= self.prob_mutacion:
                """ print(f'\n\neste es el hijo 2\n{hijo2}\n\n') """
                hijo1 = self.mutacion_gen(hijo2)
                """ print(f'\n\neste es el hijo mutado 2\n{hijo2}\n\n') """
                """ print(pob_nueva[-1]) """
                pob_nueva.extend([hijo1, hijo2])
                    # Calcular y guardar los datos del peor individuo, el mejor y la media
            fitness_pob = [self.diferencia(i) for i in pob_nueva]
            peor_individuo = min(fitness_pob)
            mejor_individuo = max(fitness_pob)
            media_poblacion = np.mean(fitness_pob)
            peores_individuos.append(peor_individuo)
            mejores_individuos.append(mejor_individuo)
            medias.append(media_poblacion)
        pob_nueva = self.poda(pob_nueva)
        self.pob = pob_nueva[:self.pob_max]
        return peores_individuos, mejores_individuos, medias
        

    def poda(self,pob_nueva):
         
        tolerancia_relativa = 0.01
        numeroObjetivo = self.objetivo
        lista = []
        lista2 = []
        Altos=[]
        bajos=[]
        count =0
        for x in pob_nueva:
        
            fitIndividuo= self.fitness_pro(x)
            diferencia_relativa = abs(fitIndividuo - numeroObjetivo) / abs(numeroObjetivo)
            """ print(diferencia_relativa) """
            if diferencia_relativa <= tolerancia_relativa:
                lista.append (x)
                Altos.append(fitIndividuo)
                """ print(f'el numero {count} sobrevivio ') """
            elif diferencia_relativa>= tolerancia_relativa:
                lista2.append (x)
                bajos.append(fitIndividuo)

            count+=1
        count1=0
        datos=[]
        for i in lista:
            for x in i:
                count1 += 1
                if count1 < 30:
                    #print(self.alimentos[x].nombre,self.alimentos[x].categoria, self.alimentos[x].energia,self.alimentos[x].proteinas,self.alimentos[x].grasa,self.alimentos[x].calcio,self.alimentos[x].hierro,self.alimentos[x].vitamina_a,self.alimentos[x].tiamina,self.alimentos[x].riboflavina,self.alimentos[x].niacina,self.alimentos[x].folato,self.alimentos[x].vitamina_c)
                    datos.extend([self.alimentos[x].nombre,self.alimentos[x].categoria, self.alimentos[x].energia,self.alimentos[x].proteina,self.alimentos[x].grasa,self.alimentos[x].calcio,self.alimentos[x].hierro,self.alimentos[x].vitamina_a,self.alimentos[x].tiamina,self.alimentos[x].riboflavina,self.alimentos[x].niacina,self.alimentos[x].folato,self.alimentos[x].vitamina_c])

        print(datos)
        ruta_archivo = "tabla_alimentos.csv"
        tabla = TablaAlimentos(datos)
        tabla.mostrar()
        tabla.guardar_datos_csv(ruta_archivo)
        return lista
        
    def mostrar_tabla(self):
        

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
        for fila in self.datos:
            tree.insert("", "end", values=fila)

        # Agregar el Treeview a la ventana
        tree.pack()

        # Iniciar el bucle de eventos
        ventana.mainloop()
 
    def setAlimentos (self,alimentos):
        self.setAlimentos = alimentos
    
    def completar_lista(self,lista):
        repetidos = []
        resultado = []

        for numero in lista:
            if numero not in resultado:
                resultado.append(numero)
            else:
                repetidos.append(numero)
        """ print(f'los numeros repetidos son {repetidos[:]}\n') """
        
        numeros_faltantes = set(range(1, 115)) - set(resultado)
        numeros_faltantes = sorted(list(numeros_faltantes))
        # print(f'los numeros faltantes son {numeros_faltantes}')
        # random.shuffle(numeros_faltantes)
        # print(f'los numeros faltantes son {numeros_faltantes}')
        for numero in repetidos:
            resultado.append(numeros_faltantes.pop(0))
 
        return resultado


    def mutacion_gen(self, individuo):
        individuo_mutado = individuo # Hacer una copia del individuo original

        for i in range(len(individuo_mutado)):
            numero = random.randint(0, 113)

            if random.uniform(0, 1) <= self.prob_genes:
                individuo_mutado = self.intercambiar_posiciones(individuo_mutado, i, numero)

        return individuo_mutado  # Retornar el individuo mutado


    def intercambiar_posiciones(self, individuo, pos1, pos2):
        lista = individuo  # Hacer una copia del individuo original
        lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
        return lista

def inicializar():

    pob_inicial = int(pob_init.get())
    pob_max = int(Pob_max.get())
    prob_cruza = float(Prob_cruza.get())
    prob_mutacion = float(Prob_mutacion.get())
    prob_genes = float(Prob_genes.get())
    objetivo = int(Objetivo.get())
    enfoque_input  = enfoque.get()
    mi_mochila= mochila(pob_inicial,pob_max,prob_cruza,prob_mutacion,prob_genes,enfoque_input ,objetivo)

    peores_individuos, mejores_individuos, medias=mi_mochila.generaciones()
    graficar(peores_individuos, mejores_individuos, medias)
    
 
def graficar(peores_individuos, mejores_individuos, medias):
    generacion = range(len(peores_individuos))
    plt.plot(generacion, peores_individuos, label="Peor Individuo")
    plt.plot(generacion, mejores_individuos, label="Mejor Individuo")
    plt.plot(generacion, medias, label="Media")

    plt.xlabel("Generación")
    plt.ylabel("Fitness")
    plt.title("Evolución del Fitness")
    plt.legend()
    plt.show()
                



# Llamar a la función para mostrar la tabla

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

Pob_max = tk.Entry(root,width=30,font=fuente2, bg="#7ce2cc", bd=0, highlightthickness=2, highlightbackground="black")
Pob_max.place(x=330, y=205)

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

button = tk.Button(root, text="Obtener", font=fuente, bg="#72B960", fg="white",command=inicializar)
button.place(x=756, y=508, width=187, height=60)

label_7 = tk.Label(root, text="Rellene los siguientes campos", font=fuente3,  bg="#F5F190", fg="#1E1E1E")
label_7.place(x=150, y=10, width=700, height=50)
root.geometry("1000x600")
root.mainloop() 


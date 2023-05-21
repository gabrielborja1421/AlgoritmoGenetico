import random
import numpy as np
from Alimentos import *
from PyQt5 import QtWidgets, uic

class mochila:

    def __init__(self,pob_inicial,pob_max,prob_cruza,prob_mutacion,prob_genes,fitness,nSeleccionados,objetivo):

        self.pob = pob_inicial
        self.pob_max = pob_max
        self.prob_cruza = prob_cruza
        self.prob_mutacion = prob_mutacion
        self.prob_genes = prob_genes
        self.fitness = fitness
        self.nSeleccionados = nSeleccionados
        self.MaxMochila = 3000
        self.objetivo= 1000

    def generar_individuo (self, cantidad):
        rango = list(range(1,115))
        random.shuffle(rango)
        individuo = rango[:cantidad]
        return individuo


 

    def fitness_pro(self,individuo):
        """ print(individuo) """
        energia_total= 0
        count=0
        for i in range(len(individuo)):
            count+=1
            numero = individuo[i]
            if count<30:
                energia_total= energia_total +alimentos[numero].energia
        """ print(energia_total) """
        return energia_total

    def seleccion(self,poblacion):
        """ 
        seleccion por competicion

        """
        score = [(self.fitness_pro(i), i) for i in poblacion]
        #score = [(i[0], i[1]) for i in sorted(score) ]
        score = [ i[1] for i in sorted(score) ]
        seleccionados = score [len (score) - self.nSeleccionados :]
        self.seleccionados = seleccionados
        """ print(seleccionados) """
       

        return(seleccionados)
        
    def crear_pob_inicial (self,poblacion):
        pob = []
        for x in range(poblacion):
            pob.append(self.generar_individuo(114))
        return pob
            
    def cruza(self,poblacion , seleccionados ):
        fathers=[]
        fathers = random.sample(seleccionados, 2)
        longitud = min(len(fathers[0]), len(fathers[1]))
        cruza = random.randint(1, longitud -1)

        hijo1 = fathers[0][:cruza] + fathers[1][cruza:]
        hijo2 = fathers[1][: cruza] + fathers[0] [cruza:]
        """ print(f'el padre numero 1 es {fathers[0]}\n\n el padre 2 es: {fathers[1]}\n\n')
        print(f'el hijo numero 1 es {hijo1} \n\n el hijo 2 es {hijo2}') """
        hijo1=self.completar_lista(hijo1)
        hijo2=self.completar_lista(hijo2)
        """ print(f'hijo uno : {hijo1} \n\n hijo dos: {hijo2}') """
        
        return hijo1, hijo2
      

    def mutacion (self, poblacion):
        for i in range(len(poblacion)):
            if random.random() <= self.prob_mutacion:
                point = random.randint(1, len(poblacion[i]) - 1)
                new_value = np.random.randint(0, 9)

                while new_value == poblacion[i][point]:
                    new_value = np.random.randint(0, 9)
                poblacion[i][point] = new_value

        return poblacion


    def listaDecruza (self, lista1,lista2):
        longitud = min(len(lista1), len(lista2))
        cruza = random.randint(1, longitud -1)

        hijo1 = lista1[:cruza] + lista2[cruza:]
        hijo2 = lista2 [: cruza] + lista1 [cruza:]
        
        return hijo1, hijo2
    
    def generaciones(self):
        pob_nueva = self.crear_pob_inicial(self.pob)
        hijo1 = None
        hijo2 = None
        print(alimentos[0].energia)
        while len(pob_nueva) < self.pob_max:
            print (pob_nueva)
            if random.uniform(0, 1) <= self.prob_cruza:
                hijo1, hijo2 = self.cruza(pob_nueva, self.seleccion(pob_nueva))
            if random.uniform(0, 1) <= self.prob_mutacion:
                hijo1 = self.mutacion_gen(hijo1)
            if random.uniform(0, 1) <= self.prob_mutacion:
                hijo2 = self.mutacion_gen(hijo2)
            if hijo1!=None and hijo2 != None:
                pob_nueva.extend([hijo1, hijo2])
            # self.poda(pob_nueva)
        self.pob = pob_nueva[self.pob_max]

    def poda(self,pob_nueva):
        tolerancia_relativa = 0.50
        numeroObjetivo = self.objetivo
        lista = []
        count =0
        for x in pob_nueva:
            
            fitIndividuo= self.fitness_pro(x)
            diferencia_relativa = abs(fitIndividuo - numeroObjetivo) / abs(numeroObjetivo)
            if diferencia_relativa <= tolerancia_relativa:
                lista.append(x)
                """ print(f'el numero {count} sobrevivio ') """
            count+=1
            
        return lista
        
        
 
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
        """ print(f'los numeros faltantes son {numeros_faltantes}') """
        for numero in repetidos:
            resultado.append(numeros_faltantes.pop(0))
 
        return resultado
        
    def mutacion_gen(self,individuo):
        for i in range(len(individuo)):
            numero= random.randint(0,113)

            if random.uniform(0,1) <= self.prob_genes:
                self.intercambiar_posiciones(individuo,i,numero)


    def intercambiar_posiciones(self,individuo, pos1, pos2):
        lista=[]
        """ print(f'pos1 es {pos1}\n\n pos2 es {pos2}') """
        """    print (len(individuo))
        print(f'el intercambio sera {pos1} a {pos2}') """
        lista.extend(individuo)
        """ print(len(lista),len(individuo)) """
        lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
        #print(f'antes de la mutacion de gen : \n\n {individuo} \n despues de la mutacion \n\n {lista}')
""" 
#iniciar aplicacion
app = QtWidgets.QApplication([])

# cargar archivo .ui
home = uic.loadUi("home.ui")


#ejecutar 
home.show()
app.exec() """

alimentos = []
df = pd.read_excel("dataset alimentos.xlsx")


for index, row in df.iterrows():
    alimento = Alimento(row['Alimento'], row['Categoria'], row['Energía'], row['Proteína'], row['Grasa'], row['Calcio'], row['Hierro'], row['Vitamina A'], row['Tiamina'], row['Riboflavina'], row['Niacina'], row['Folato'], row['Vitamina C'])
    alimentos.append(alimento)
        

mochila= mochila(10,20,.5,.4,.6,0,4,1000)
mochila.setAlimentos(alimentos)
mochila.generaciones()






""" def se_aproxima(num_aleatorio, num_objetivo, tolerancia):
    diferencia = abs(num_aleatorio - num_objetivo)
    if diferencia <= tolerancia:
        return True
    else:
        return False """
""" def se_aproxima(num_aleatorio, num_objetivo, tolerancia_relativa):
    diferencia_relativa = abs(num_aleatorio - num_objetivo) / abs(num_objetivo)
    if diferencia_relativa <= tolerancia_relativa:
        return True
    else:
        return False """




#generar_num_aleatorios = mochila(1,1,1,1,1,1) 







# list1 = [] 
# list2 = []
# list1.extend(generar_num_aleatorios.numerosAleatorios(114)) #generamos numeros aleatorios y se las asignamos a list1
# print(f' La lista 1 es : {list1[:]}')#imprimimos todo el contenido de list1
# list2.extend(generar_num_aleatorios.numerosAleatorios(114))
# print(f' la lista 2 es : {list2[:]}')

# #print(f'el numero de aletorios es : {generar_num_aleatorios.numerosAleatorios(3)} y el numero de aleatorios 2 es : {generar_num_aleatorios2.numerosAleatorios(5)}')


"""     def cruza(self,poblacion , seleccionados ):
        point = 0
        fathers=[]
        for i in range(len(poblacion)):
            point = np.random.randint(1,len(seleccionados)- 1)
            fathers = random.sample(seleccionados, 2)
            print(f'antes de la cruza \n{fathers[:]}')
            poblacion[i][:point] = fathers[0][:point]
            poblacion[i][point:] = fathers [1][point:]
        print(f'despues de la cruza \n{fathers[:]}')
        return poblacion """








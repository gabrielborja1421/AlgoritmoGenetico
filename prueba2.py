import random
import numpy as np
from Alimentos import *
from PyQt5 import QtWidgets, uic

class Mochila:
    def __init__(self, pob_inicial, pob_max, prob_cruza, prob_mutacion, prob_genes, fitness, nSeleccionados, objetivo):
        self.pob = pob_inicial
        self.pob_max = pob_max
        self.prob_cruza = prob_cruza
        self.prob_mutacion = prob_mutacion
        self.prob_genes = prob_genes
        self.fitness = fitness
        self.nSeleccionados = nSeleccionados
        self.MaxMochila = 3000
        self.objetivo = objetivo

    def generar_individuo(self, cantidad):
        rango = list(range(1, 115))
        random.shuffle(rango)
        individuo = rango[:cantidad]
        return individuo

    def fitness_pro(self, individuo):
        energia_total = 0
        count = 0
        for i in range(len(individuo)):
            count += 1
            numero = individuo[i]
            if count < 30:
                energia_total += alimentos[numero].energia
        return energia_total

    def seleccion(self, poblacion):
        score = [(self.fitness_pro(i), i) for i in poblacion]
        score = [i[1] for i in sorted(score)]
        seleccionados = score[len(score) - self.nSeleccionados :]
        return seleccionados

    def crear_pob_inicial(self, poblacion):
        pob = []
        for x in range(poblacion):
            pob.append(self.generar_individuo(114))
        return pob

    def cruza(self, poblacion, seleccionados):
        fathers = random.sample(seleccionados, 2)
        longitud = min(len(fathers[0]), len(fathers[1]))
        cruza = random.randint(1, longitud - 1)

        hijo1 = fathers[0][:cruza] + fathers[1][cruza:]
        hijo2 = fathers[1][:cruza] + fathers[0][cruza:]

        hijo1 = self.completar_lista(hijo1)
        hijo2 = self.completar_lista(hijo2)

        return hijo1, hijo2

    def mutacion(self, poblacion):
        for i in range(len(poblacion)):
            if random.random() <= self.prob_mutacion:
                point = random.randint(1, len(poblacion[i]) - 1)
                new_value = np.random.randint(0, 9)

                while new_value == poblacion[i][point]:
                    new_value = np.random.randint(0, 9)
                poblacion[i][point] = new_value

        return poblacion

    def listaDecruza(self, lista1, lista2):
        longitud = min(len(lista1), len(lista2))
        cruza = random.randint(1, longitud - 1)

        hijo1 = lista1[:cruza] + lista2[cruza:]
        hijo2 = lista2[:cruza] + lista1[cruza:]

        return hijo1, hijo2

    def generaciones(self):
        pob_nueva = self.crear_pob_inicial(self.pob)
        while len(pob_nueva) < self.pob_max:
            if random.uniform(0, 1) <= self.prob_cruza:
                hijos = self.cruza(pob_nueva, self.seleccion(pob_nueva))
                pob_nueva.append(hijos[0])
                if len(pob_nueva) < self.pob_max:
                    pob_nueva.append(hijos[1])

            pob_nueva = self.mutacion(pob_nueva)
        return pob_nueva

    def completar_lista(self, lista):
        while len(lista) < 114:
            lista.append(np.random.randint(0, 9))
        return lista

app = QtWidgets.QApplication([])
mochila = Mochila(10, 50, 0.8, 0.01, 0.1, 30, 3, 100)
poblacion_final = mochila.generaciones()
print(poblacion_final)

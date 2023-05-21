import random
import numpy as np


class AlgoritmoGenético:
    def __init__(self, pob_inicial, pob_max, prob_cruza, prob_mutacion, prob_genes, fitness):
        self.pob = pob_inicial
        self.pob_max = pob_max
        self.prob_cruza = prob_cruza
        self.prob_mutacion = prob_mutacion
        self.prob_genes = prob_genes
        self.fitness = fitness
        self.poblacion_inicial=[]

    def seleccionar(self):
        fitness = [self.fitness(i) for i in self.pob]
        fitness_suma = sum(fitness)
        prob = [f / fitness_suma for f in fitness]
        i_padres = np.random.choice(
            len(self.pob), size=2, replace=False, p=prob)
        return self.pob[i_padres[0]], self.pob[i_padres[1]]

    def cruza(self, padres):
        if random.random() < self.prob_cruza:
            punto_cruza = random.randint(1, len(padres[0]) - 1)
            hijo1 = padres[0][:punto_cruza] + \
                padres[1][punto_cruza:]
            hijo2 = padres[1][:punto_cruza] + \
                padres[0][punto_cruza:]
            return hijo1, hijo2
        return padres[0], padres[1]

    def mutar(self, individuo):
        mutados = []
        for gen in individuo:
            if random.random() < self.prob_genes:
                mutados.append(1 - gen)
            else:
                mutados.append(gen)
        return mutados

    def generacion(self):
        pob_nueva = []
        while len(pob_nueva) < self.pob_max:
            padres = self.seleccionar()
            hijo1, hijo2 = self.cruza(padres)
            if random.random() < self.prob_mutacion:
                hijo1 = self.mutar(hijo1)
            if random.random() < self.prob_mutacion:
                hijo2 = self.mutar(hijo2)
            pob_nueva.extend([hijo1, hijo2])
        self.pob = pob_nueva[:self.pob_max]

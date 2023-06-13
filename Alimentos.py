import pandas as pd


class Alimento:
    def __init__(self, Alimento, Categoria, Energía, Proteina, Grasa, Calcio, Hierro, Vitamina_A, Tiamina, Riboflavina, Niacina, Folato, Vitamina_C):
        self.nombre = Alimento
        self.categoria = Categoria
        self.energia = Energía
        self.proteina = Proteina
        self.grasa = Grasa
        self.calcio = Calcio
        self.hierro = Hierro
        self.vitamina_a = Vitamina_A
        self.tiamina = Tiamina
        self.riboflavina = Riboflavina
        self.niacina = Niacina
        self.folato = Folato
        self.vitamina_c = Vitamina_C
  

    def crear (self):
        alimentos = []
        df = pd.read_excel("dataset alimentos.xlsx")


        for index, row in df.iterrows():
            alimento = Alimento(row['Alimento'], row['Categoria'], row['Energía'], row['Proteína'], row['Grasa'], row['Calcio'], row['Hierro'], row['Vitamina A'], row['Tiamina'], row['Riboflavina'], row['Niacina'], row['Folato'], row['Vitamina C'])
            alimentos.append(alimento)
        
        return alimentos


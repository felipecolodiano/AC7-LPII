from .vaccine import Vaccine, Intra_muscular, Intra_venosa, Superficie
from ..Exceptions.exceptions import TipoVacinaInvalido 

class Animal(object):
    def __init__(self,peso,cor,registro):
        self.peso = peso
        self.cor = cor
        self.registro = registro
        
    def recebe_vacina(self):
        return "Recebe vacina de forma GENERICA"

class Gato(Animal):
    def __init__(self,peso,cor,registro):
        Animal.__init__(self,peso,cor,registro)
        
    def recebe_vacina(self):
        return f"Vacina: Intra-Muscular, peso:{self.peso}, cor:{self.cor}, RGA:{self.registro}"

class Cachorro(Animal):
    def __init__(self,peso,cor,registro):
        Animal.__init__(self,peso,cor,registro)
        
    def recebe_vacina(self):
        return f"Vacina: Intra-Venosa, peso:{self.peso}, cor:{self.cor}, RGA:{self.registro}"

class Cavalo(Animal):
    def __init__(self,peso,cor,registro):
        Animal.__init__(self,peso,cor,registro)
       
    def recebe_vacina(self):
        return f"Vacina: Superficie, peso:{self.peso}, cor:{self.cor}, RGA:{self.registro}"


lista = [Cachorro(30, 'preto', 1203), Gato(4, 'branco', 1200), Cavalo(1000, 'marrom',1345)]
for animal in lista:
    print(animal.recebe_vacina())

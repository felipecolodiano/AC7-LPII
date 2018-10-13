from .vacinas import IntraMuscular, IntraVenosa, Superficie
from ..excpetions.excpetions import TipoVacinaInvalido

class Animal(object):
    def __init__(self, cor, especie, peso, idade):
        self.cor = cor
        self.especie = especie
        self.peso = peso
        self.idade = idade

class Gato(Animal):
    def __init__(self, cor, especie, peso, idade):
        Animal.__init__(self, cor, especie, peso, idade)

    def receberVacina(self, tipo):
        pass

class Cachorro(Animal):
    def __init__(self, cor, especie, peso, idade):
        Animal.__init__(self, cor, especie, peso, idade)

    def receberVacina(self, tipo):
        pass

class Cavalo(Animal):
    def __init__(self, cor, especie, peso, idade):
        Animal.__init__(self, cor, especie, peso, idade)

    def receberVacina(self, tipo):
        pass

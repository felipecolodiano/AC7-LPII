from animais import Animal, Gato, Cachorro, Cavalo
from ..exceptions.exceptions import TipoVacinaInvalido

class Vacina():
    def __init__(self, tipo, dose):
        self.tipo = tipo
        self.dose = dose

class IntraMuscular():
    def tipo(self):       
        return 'Intra Muscular'

class IntraVenosa():
    def tipo(self):       
        return 'Intra Venosa'


class Superficie():
    def tipo(self):       
        return 'Surpeficie'
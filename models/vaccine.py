from .animals import Animal, Gato, Cachorro, Cavalo
from ..Exceptions.exceptions import TipoVacinaInvalido

class Vaccine(object):
    def __init__(self,tipo,dose):
        self.tipo = tipo
        self.dose = dose

    def vacinar(self):
        return "Vacinando de forma GENERICA"

#vacina Gato 
class Intra_muscular(Vaccine):
    def vacinar(self, animal, vacina):
        try:
            if animal == vacina:
                raise f'Vacina: {self.tipo}, Dose: {self.dose}ml'
            else:
                return animal != vacina
        except TipoVacinaInvalido as e:
            print(e)

    def __str__(self):
        return "Aplicando..."


#vacina Cachorro
class Intra_venosa(Vaccine):
    def vacinar(self, animal, vacina):
        try:
            if animal == vacina:
                raise f'Vacina: {self.tipo}, Dose: {self.dose}ml'
            else:
                return animal != vacina
        except TipoVacinaInvalido as e:
            print(e)
        
    def __str__(self):
        return "Aplicando..."

#vacina Cavalo
class Superficie(Vaccine):
    def vacinar(self, animal, vacina):
        try:
            if animal == vacina:
                raise f'Vacina: {self.tipo}, Dose: {self.dose}ml'
            else:
                return animal != vacina
        except TipoVacinaInvalido as e:
            print(e)

    def __str__(self):
        return "Aplicando..."

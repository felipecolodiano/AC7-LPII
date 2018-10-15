from vacinas import Intramuscular, Intravenosa, Superficie
from ..exceptions.exceptions import TipoVacinaInvalido

class Animal ():
    def vacinar_animal (self):
        return "Receber vacina do tipo GENÉRICO"


class Gato (Animal):
    def vacinar_animal (self):
        return "Receber vacina do tipo INTRAMUSCULAR"


class Cachorro (Animal):
    def vacinar_animal (self):
        return "Receber vacina do tipo INTRAVENOSA"


class Cavalo (Animal):
    def vacinar_animal (self):
        return "Receber vacina do tipo SUPERFICIAL"

lista = [Gato(), Cachorro(), Cavalo()]
for Animal in lista:
    print(Animal.vacinar_animal())

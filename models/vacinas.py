from animais import Animal, Gato, Cachorro, Cavalo
from ..exceptions.exceptions import TipoVacinaInvalido

class Vacina ():
    def aplicar_vacina (self):
        return "Aplicar vacina na espécie GENÉRICA"


class Intramuscular (Vacina):
    def aplicar_vacina (self):
        return "Aplicar vacina na espécie GATO"


class Intravenosa (Vacina):
    def aplicar_vacina (self):
        return "Aplicar vacina na espécie CACHORRO"


class Superficie (Vacina):
    def aplicar_vacina (self):
        return "Aplicar vacina na espécie CAVALO"

lista = [Intramuscular(), Intravenosa(), Superficie()]
for Vacina in lista:
    print(Vacina.aplicar_vacina())

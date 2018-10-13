class TipoVacinaInvalido(Exception):
    def __init__(self,tipo):
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo}"

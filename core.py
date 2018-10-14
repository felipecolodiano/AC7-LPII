#from Business import *
from Business.animals import Animal, Gato, Cachorro, Cavalo
from Business.vaccine import Vaccine, Intra_muscular, Intra_venosa, Superficie

def main():
    print("Bem-vindo ao controle de Zoonoses de São Paulo")
    print("Escolha uma das opções abaixo para vacinação: ")
    print('1 - Cachorro')
    print('2 - Cavalo')
    print('3 - Gato')
    
    optAnimal = int(input('DIGITE O N° DA OPERAÇÃO DESEJADA:>>>>'))

    print("Escolha uma das opções do tipo de vacina: ")
    print('1 - Intra-Venosa')
    print('2 - Superficie')
    print('3 - Intra-Muscular')

    optVaccine = int(input('DIGITE O N° DA OPERAÇÃO DESEJADA:>>>>'))


    if optAnimal == 1 and optVaccine == 1:
        return Vaccine().Intra_venosa(animal, vacina)
    elif optAnimal == 2 and optVaccine == 2:
        return Vaccine().Superficie(animal, vacina)
    elif optAnimal == 3 and optVaccine == 3:
        return Vaccine().Intra_muscular(animal, vacina)
    else:
        print('OPIÇÃO INVÁLIDA!!!')
        return main()

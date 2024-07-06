import random

#classe elementar
class Elemento:
    _id_counter = 0
    def __init__(self, nome: str, cidade: str, comida: str, altura: float):
        Elemento._id_counter += 1
        self.__id = Elemento._id_counter
        self.__nome = nome
        self.__cidade = cidade
        self.__comida = comida
        self.__altura = altura

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def comida(self):
        return self.__comida
    
    @property
    def altura(self):
        return self.__altura


from abc import ABC, abstractmethod
class Animal(ABC):
    def _init_(self, especie, raca, nome, cor, idade):
        self.especie = especie
        self.raca = raca
        self.nome = nome
        self.cor = cor
        self.idade = idade

    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def morder(self):
        pass

    @abstractmethod
    def correr(self):
        pass

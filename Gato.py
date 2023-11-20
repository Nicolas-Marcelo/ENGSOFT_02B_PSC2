from Animal import Animal
class Gato(Animal):
    def _init_(self, especie, raca, nome, cor, idade, pelo, garra):
        super()._init_(especie, raca, nome, cor, idade)
        self.pelo = pelo
        self.garra = garra

    def emitir_som(self):
        print(f'O {self.nome} esta miando!')

    def morder(self):
        print(f'O {self.nome} mordeu um funcionario!')

    def correr(self):
        print(f'O {self.nome} esta correndo, se divertindo!')

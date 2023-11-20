from Animal import Animal
class Cachorro(Animal):
    def _init_(self, especie, raca, nome, cor, idade, vacinas, pelo, garra):
        super()._init_(especie, raca, nome, cor, idade)
        self.vacinas = vacinas
        self.pelo = pelo

    def emitir_som(self):
        print(f'O {self.nome}, está latindo')

    def morder(self):
        print(f'O {self.nome} acaba de morder um funcionario!')

    def correr(self):
        print(f'O {self.nome} está correndo, se divertindo!')

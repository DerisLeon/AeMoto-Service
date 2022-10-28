from model.funcionario import Funcionario


class Motorista(Funcionario):

    def __init__(self, rotas, funcionario):
        self.funcionario = funcionario
        self.rotas = rotas

    def __repr__(self):
        return '\nRotas: {}\n'.format(self.rotas)
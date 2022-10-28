class Funcionario():
    
    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo

    def __repr__(self):
        return '\nPrefeitura: {}\n Cargo: {}'.format(self.prefeitura, self.cargo)

    
from model.pessoa import Pessoa

class GestorApp(Pessoa):
    
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def __repr__(self):
        return '\nGestorApp: {}\n'.format(self.pessoa)
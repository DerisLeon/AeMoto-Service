class Rota():
    
    
    def __init__(self, nomeDestino, qtdalunos, prefeitura, veiculo, passageiro, horaSaida, horaChegada):
        self.nomeDestino = nomeDestino
        self.qtdalunos = qtdalunos
        self.prefeitura = prefeitura        
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada = horaChegada

    def __repr__(self):
        return '\nNome destino: {}\n  Quantidade de Alunos: {}\n Prefeitura: {}\n Veículo: {}\n Passageiro: {}\n Hora de Saída: {}\n Hora de chegada: {}\n'.format(self.nomeDestino, self.qtdalunos, self.prefeitura, self.veiculo, self.passageiro, self.horaSaida, self.horaChegada)
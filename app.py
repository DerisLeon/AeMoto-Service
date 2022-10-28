from model.aluno import Aluno
from model.cidade import Cidade
from model.endereco import Endereco
from model.funcionario import Funcionario
from model.gestorApp import GestorApp
from model.instituicaoDeEnsino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.pessoa import Pessoa
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.uf import Uf
from model.veiculo import Veiculo



pessoa = Pessoa("Juvenal", "25/11/2001", "juvenal@gmail.com", "22222-2222")
pessoa2 = Pessoa("Rhavy", "15/03/1980", "rhavy@gmail.com", "111111-1111")

aluno = Aluno("Déris", "17/11/2001", "deris@gmail.com", "333333-3333", "IFPB", "TSI", "20009389")

cidade = Cidade("Guarabira", "GBA")
endereco = Endereco("58200-000", "13", "Casa", "Próximo a vitória", "Rua do Jair Embora")

prefeitura = Prefeitura("Mateus", "mateus@gmail.com", "44444-4444", "Marcos Diogo")
funcionario = Funcionario(prefeitura, "Técnico")

veiculo = Veiculo("Guarabira", "20", "Ônibus", "PT-1313")

gestor = GestorApp(pessoa2)

instituicao = InstituicaoDeEnsino("IFPB", "Rodovia km52", "32323-3232")

rota = Rota("Guarabira", "50", "Pirpirituba", "Mini Van", "Gleidson", "07:00h", "10:00h")
motorista = Motorista(rota, funcionario)
print(rota, motorista)

passageiro = Passageiro(aluno, "Pirpirituba", "Guarabira")
print(passageiro)

prefeito = Prefeito(pessoa)
uf = Uf("Paraíba", "PB")

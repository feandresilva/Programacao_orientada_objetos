# Um laboratório de coleta de sangue precisa de um sistema para organizar os atendimentos realizados 
# na recepção. Os pacientes devem ser atendidos por ordem de chegada, 
# recebendo automaticamente um número sequencial no momento do cadastro. 
# Depois de cadastrado, cada paciente deverá ser colocado no final da fila 
# e aguardar até ser chamado para a coleta.

# Crie as classes Paciente, Exame e Atendimento. 
# 
# A classe Paciente deverá possuir os atributos nome, CPF, data_nascimento e numero_atendimento, 
# além do método exibir_dados. 
# 
# A classe Exame deverá possuir os atributos codigo, nome, preco e necessita_jejum, 
# além dos métodos exibir_dados e exibir_preparo. 
# 
# A classe Atendimento deverá armazenar o paciente, uma lista de exames e a situação atual do atendimento.
#  Ela também deverá manter a fila de pacientes, gerar automaticamente os números de atendimento 
# e possuir os métodos adicionar_exame, calcular_total, entrar_na_fila, chamar_proximo, iniciar_coleta, 
# finalizar_atendimento e exibir_resumo.

# Faça um programa com um menu que permita cadastrar um novo paciente, 
# incluir seus exames, adicionar o atendimento ao final da fila, visualizar a fila 
# na ordem de chegada, chamar o próximo paciente, iniciar a coleta e finalizar o atendimento. 
# Quando um paciente for chamado, ele deverá ser removido do início da fila. 
# O número de atendimento deverá começar em 1 e ser incrementado automaticamente a cada novo 
# cadastro. O programa deverá continuar funcionando até que o usuário escolha a opção de encerrar.

class Paciente:
    nome: str
    cpf: int
    numero_atendimento: int
    data_nascimento: str

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Data de Nascimento: {self.data_nascimento}')
        print(f'CPF: {self.cpf}')
        print(f'Número do atendimento: {self.numero_atendimento}')


class Exame:
    codigo: int
    nome: str
    preco: float
    necessita_jejum: bool
    preparo: str

    def exibir_dados(self):
        print(f'Código: {self.codigo}')
        print(f'Nome: {self.nome}')
        print(f'Preço: R${self.preco}')
        print(f'Necessidade de Jejum: {self.necessita_jejum}')

    def exibir_preparo(self):
        print(self.preparo)


class Atendimento:
    paciente: str
    lista_exames: list
    situacao_atual: str
    fila_pacientes: int
    gerar_numeros_atendimentos: int

    def adicionar_exames(self, exame):
        self.lista_exames.append(exame)

    def calcular_total(self):
        soma = 0
        for exame in self.lista_exames:
            soma += exame.preco
        return soma

    def entrar_na_fila(self, paciente):
        self.numero_atendimento.append(self.fila_pacientes)
        
    
    def chamar_proximo(self):
    

    def iniciar_coleta(self):


    def _finalizar_atendimento(self):


    def exibir_resumo(self):

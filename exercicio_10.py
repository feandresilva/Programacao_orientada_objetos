# A academia FitLife precisa de um sistema para auxiliar o trabalho da recepção. 
# O sistema deverá permitir o cadastro dos alunos, armazenando informações como nome, CPF, 
# data de nascimento, telefone, endereço e número da matrícula.

# Cada aluno deverá possuir uma matrícula com informações como data de início, 
# data de vencimento e status. O status poderá indicar se a matrícula está ativa, inadimplente 
# ou cancelada. Antes de liberar o acesso à academia, a recepção deverá consultar 
# o aluno e verificar se sua matrícula permite a entrada.

# O sistema também deverá registrar as entradas e saídas dos alunos, 
# armazenando a data e o horário de cada movimentação. 
# A identificação poderá ser realizada pela carteirinha ou pelo CPF. 
# Caso o aluno esteja sem a carteirinha, a recepção deverá validar sua identidade 
# utilizando seus dados cadastrados antes de realizar uma liberação temporária.

# Crie o sistema utilizando programação orientada a objetos em Python.
# O sistema deverá salvar todos os dados em arquivos (pickle ou json), 
# e cada ação executada deverá ser salva e registrada.
# O sistema deve ser resiliente a erros e a entradas incorretas/inválidas. 
# Exiga uma autenticação (usuário e senha) para as ações administrativas do sistema 
# (adicionar aluno, alterar matrícula, registrar entrada/saída, etc).

import pickle
from datetime import date
from datetime import datetime

class Aluno:

    def __init__(self, nome, cpf, data_nascimento, telefone, endereco, numero_matricula):
        self.nome = nome
        self.cpf = cpf
        if type(cpf) != str:
            raise ValueError("O CPF precisa ser uma string!")
        self.data_nascimento = data_nascimento
        if type(data_nascimento) != date:
            self.data_nascimento = date.fromisoformat(data_nascimento) #aaaa-mm-dd
        self.telefone = telefone
        if type(telefone) != int:
            raise ValueError("O número de telefone precisa ser um inteiro (números)")
        self.endereco = endereco
        if type(endereco) != str:
            raise ValueError("O endereço deve ser uma string")
        self.numero_matricula = numero_matricula
        if type(numero_matricula) != int:
            raise ValueError("O número da matrícula deve ser um inteiro (números)")

    def __str__(self):
        return (f'Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, CPF: {self.cpf}, Telefone: {self.telefone}, Número da Matrícula: {self.numero_matricula}')

    def registrar_entrada(self):
        with open("registro_atividade_academia.log", "a") as f:
            f.write(f'{datetime.now()}, o aluno {self.nome}, matrícula nº{self.numero_matricula}, entrou na academia.\n')
            print("Arquivo salvo com sucesso!")

    def registrar_saida(self):
        with open("registro_atividade_academia.log", "a") as f:
            f.write(f'{datetime.now()}, o aluno {self.nome}, matrícula nº {self.numero_matricula}, saiu da academia\n')

class Matricula:
    data_inicio: str
    data_vencimento: str
    status = []

    def __init__(self):
        self.status = ["Ativa", "Inadimplente", "Cancelada"]

    

def cadastrar_aluno():
    while True:
        nome = input("Por favor, insira o nome do novo aluno: ").strip().capitalize()
        cpf = (input("Por favor, insira o CPF do novo aluno: "))
        data_nascimento = input("Por favor, insira a data de nascimento do novo aluno (aaaa-mm-dd): ")
        telefone = int(input("Por favor, insira o telefone do novo aluno: "))
        endereco = input("Por favor, insira o endereço do novo aluno: ")
        numero_matricula = int(input("Por favor, insira o número da matrícula do novo aluno: "))
        novo_aluno = Aluno(nome, cpf, data_nascimento, telefone, endereco, numero_matricula)
        return novo_aluno

#novo_aluno = cadastrar_aluno()
#novo_aluno = Aluno()

while True:
    print("MENU")
    print("1. Cadastrar novo aluno")
    print("2. Verificar matrícula")
    print("3. Alterar matrícula")
    print("4. Autorizar entrada")
    print("5. Registrar saída")
    print("6. Finalizar")

    try:
        opcao_inicial = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Por favor, insira um valor válido!")
        continue
    if opcao_inicial == 1:
        novo_aluno = cadastrar_aluno()



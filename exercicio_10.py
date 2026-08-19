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
from datetime import datetime, timedelta

class Aluno:

    def __init__(self, nome, cpf, data_nascimento, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.matricula = None
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

    def definir_matricula(self, matricula):
        self.matricula = matricula

    def __str__(self):
        return (f'Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, CPF: {self.cpf}, Telefone: {self.telefone}, Endereço: {self.endereco}')

    def registrar_entrada(self):
        with open("registro_atividade_academia.log", "a") as f:
            f.write(f'{datetime.now()}, o aluno {self.nome}, dono do CPF {self.cpf}, entrou na academia.\n')
            print("Log salvo com sucesso!")

    def registrar_saida(self):
        with open("registro_atividade_academia.log", "a") as f:
            f.write(f'{datetime.now()}, o aluno {self.nome}, dono do CPF {self.cpf}, saiu da academia.\n')
            print("Log salvo com sucesso!")

class Matricula:
    data_inicio: datetime
    data_vencimento: datetime
    status = "Ativa"

    def __init__(self):
        self.data_inicio = datetime.now()
        self.data_vencimento = self.data_inicio + timedelta(days=30)
        self.ativar_matricula()

    def cancelar_matricula(self):
        self.status = "Cancelada"
        return "A matrícula foi cancelada com sucesso!"

    def matricula_inadimplente(self):
        self.status = "Inadimplente"
        return "A matrícula está inadimplente!"

    def ativar_matricula(self):
        self.status = "Ativa"
        return "A matrícula foi ativada com sucesso!"
    

def cadastrar_aluno():
    while True:
        nome = input("Por favor, insira o nome do novo aluno: ").strip().capitalize()
        cpf = (input("Por favor, insira o CPF do novo aluno: "))
        data_nascimento = input("Por favor, insira a data de nascimento do novo aluno (aaaa-mm-dd): ")
        telefone = int(input("Por favor, insira o telefone do novo aluno: "))
        endereco = input("Por favor, insira o endereço do novo aluno: ")
        novo_aluno = Aluno(nome, cpf, data_nascimento, telefone, endereco)
        return novo_aluno

dicionario_alunos = {}

usuario = "professor_01"
senha = "senha123"


while True:
    print("MENU")
    print("1. Cadastrar novo aluno")
    print("2. Criar matrícula")
    print("3. Verificar matrícula")
    print("4. Alterar matrícula")
    print("5. Autorizar entrada")
    print("6. Registrar saída")
    print("7. Finalizar")

    try:
        opcao_inicial = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Por favor, insira um valor válido!")
        continue
    if opcao_inicial == 1:
        print("Essa ação exige usuário e senha!")
        pedindo_usuario = input("Usuário: ")
        pedindo_senha = input("Senha: ")
        if pedindo_senha != senha or pedindo_usuario != usuario:
            print("Erro! Usuário ou senha estão incorretos. Tente novamente!")
            continue
        else:
            print("Login feito com sucesso! Continue o cadastro do novo aluno!")
        novo_aluno = cadastrar_aluno()
        dicionario_alunos[novo_aluno.cpf] = novo_aluno
        print(novo_aluno)
    elif opcao_inicial == 2:
        verificar_cpf_aluno = input("Digite aqui o CPF do aluno: ")
        if verificar_cpf_aluno not in dicionario_alunos:
            print("Este aluno não está cadastrado na academia!")
        else:
            aluno = dicionario_alunos[verificar_cpf_aluno]
            aluno.definir_matricula(Matricula())
            aluno.matricula.ativar_matricula()
            print("Matrícula ativada com sucesso!")
    elif opcao_inicial == 3:
        verificar_cpf_aluno = input("Digite aqui o CPF do aluno: ")
        aluno = dicionario_alunos.get(verificar_cpf_aluno)
        if not aluno:
            print("Este aluno não está cadastrado na academia!")
        elif aluno.matricula.status == "Ativa":
            print("A matrícula está ativa!")
            print(f'Matrícula iniciada em: {aluno.matricula.data_inicio}')
            print(f'Data de vencimento: {aluno.matricula.data_vencimento}')
        elif aluno.matricula.status == "Cancelada":
            print("A matrícula está cancelada!")
        elif aluno.matricula.status == "Inadimplente":
            print("A matrícula está inadimplente!")
    elif opcao_inicial == 4:
        verificar_cpf_aluno = input("Digite aqui o CPF do aluno: ")
        aluno = dicionario_alunos.get(verificar_cpf_aluno)
        if not aluno:
            print("Este aluno não está cadastrado na academia!")
        else:
            print(f'O status da matrícula é: {aluno.matricula.status}')
            decisao_matricula = input("Digite o novo status da matrícula: ").strip().capitalize()
            if decisao_matricula == "Ativa":
                aluno.matricula.ativar_matricula()
                print("O status da matrícula foi modificado com sucesso!")
            elif decisao_matricula == "Inadimplente":
                aluno.matricula.matricula_inadimplente()
                print("O status da matrícula foi modificado com sucesso!")
            elif decisao_matricula == "Cancelada":
                aluno.matricula.cancelar_matricula()
                print("O status da matrícula foi modificado com sucesso!")
            else:
                print("Opção inválida! Tente novamente")
                continue
    elif opcao_inicial == 5:
        verificar_cpf_aluno = input("Digite aqui o CPF do aluno: ")
        aluno = dicionario_alunos.get(verificar_cpf_aluno)
        if not aluno:
            print("Este aluno não está cadastrado na academia!")
        else:
            print(f'Esse é o status da matrícula de {aluno.nome}: {aluno.matricula.status}')
            if aluno.matricula.status == "Ativa":
                print("Entrada autorizada!")
                aluno.registrar_entrada()
            elif aluno.matricula.status == "Ativa" and aluno.matricula.data_vencimento > datetime.now():
                print("Entrada não autorizada! Matrícula inadimplente.")
            else:
                print("Entrada não permitida!")
    elif opcao_inicial == 6:
        verificar_cpf_aluno = input("Digite aqui o CPF do aluno: ")
        aluno = dicionario_alunos.get(verificar_cpf_aluno)
        if not aluno:
            print("Este aluno não está cadastrado na academia!")
        else:
            print("Saída registrada!")
            aluno.registrar_saida()
    elif opcao_inicial == 7:
        print("O sistema foi encerrado com sucesso!")
        break
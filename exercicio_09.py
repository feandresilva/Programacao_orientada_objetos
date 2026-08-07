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

# Crie as classes Hemograma, Glicemia e Colesterol, herdando de Exame. 
# Cada classe deverá possuir os atributos horas_jejum e tipo_tubo, 
# definidos de acordo com o tipo do exame. 
# As classes filhas deverão sobrescrever o método exibir_preparo para mostrar 
# as orientações específicas de coleta.
# Adicione o método exibir_preparos, que deverá percorrer a lista de exames e 
# chamar o método exibir_preparo de cada objeto. 
# No menu, permita escolher o tipo de exame, 
# criar o objeto da subclasse correspondente e adicioná-lo ao atendimento do paciente.

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
    
    def iniciar_coleta(self):
        ...

class Fila:

    def __init__(self):
        self.lista_fila = []

    def entrar_na_fila(self, atendimento):
        self.lista_fila.append(atendimento)
    
    def chamar_proximo(self):   
        proximo_da_fila = self.lista_fila[0]
        del self.lista_fila[0]
        return proximo_da_fila

    def exibir_resumo(self):
        print(f'Tamanho da fila: {len(self.lista_fila)} pessoas')

class Hemograma(Exame):
    horas_jejum = "Seis horas"
    tipo_tubo = "A"

    def exibir_preparo(self):
        print("Não é necessário preparo específico")

class Glicemia(Exame):
    horas_jejum = "Seis horas"
    tipo_tubo = "A"

    def exibir_preparo(self):
        print("Seguir as orientações médicas")


class Colesterol(Exame):
    horas_jejum = "Seis horas"
    tipo_tubo = "A"

    def exibir_preparo(self):
        print("Beber água")

def cadastrar_novo_usuario():
    while True:
        novo_paciente = Paciente()
        novo_paciente.nome = input("Por favor, digite o nome do paciente: ").strip().capitalize()
        try:
            novo_paciente.cpf = int(input("Por favor, digite o CPF do paciente: "))
        except ValueError:
            print("Opção inválida! Por favor, tente novamente")
            continue
        novo_paciente.data_nascimento = input("Por favor, digite a data de nascimento do paciente: ")
        try:
            novo_paciente.numero_atendimento = input("Por favor, digite o número de atendimento do paciente: ")
        except ValueError:
            print("Opção inválida! Por favor, tente novamente")
            continue
        return novo_paciente

lista_pacientes = []
lista_de_exames = []

while True:
    print("MENU")
    print("1. Cadastrar novo paciente")
    print("2. Adicionar atendimento na fila")
    print("3. Visualizar fila")
    print("4. Chamar próximo paciente")
    print("5. Iniciar coleta")
    print("6. Finalizar atendimento")
    
    try:
        opcao_inicial = int(input("O que deseja fazer? Digite a opção escolhida: "))
    except ValueError:
        print("Opção inválida! Por favor, digite um número válido!")
        continue
    if opcao_inicial == 1:
        novo_paciente = cadastrar_novo_usuario()
        lista_pacientes.append(novo_paciente)
        novo_paciente.exibir_dados()
    elif opcao_inicial == 2:
        novo_atendimento = Atendimento()
        while True:
            print("1. Adicionar paciente")
            print("2. Adicionar exame")
            print("3. Concluir")
            try:
                decisao_menu_interno = int(input("Digite a opção desejada: "))
            except ValueError:
                print("Erro! Por favor, digite um número válido")
                continue
            if decisao_menu_interno == 1:
                checagem_cadastro_usuario = input("O usuário já está cadastrado? Digite Sim ou Não ").strip().capitalize()
                if checagem_cadastro_usuario == "Sim":
                    print(f'Lista de pacientes cadastrados: {lista_pacientes}')
                    paciente_selecionado = int(input("Selecione o índice do paciente desejado: "))
                    novo_atendimento.paciente = lista_pacientes[paciente_selecionado]
                elif checagem_cadastro_usuario == "Nao":
                    cadastrar_novo_usuario()
                    lista_pacientes.append(novo_paciente)
                    novo_paciente.exibir_dados()
            elif decisao_menu_interno == 2:
                hemograma_exame = Hemograma()
                definicao_exame = input("Qual exame deseja fazer? Hemograma, Glicemia ou Colesterol? ").strip().capitalize()
                if definicao_exame == "Hemograma":
                    hemograma_exame.codigo = input("Digite aqui o código do exame: ")
                    hemograma_exame.nome = input("Digite aqui o nome do exame: ")
                    hemograma_exame.preco = float(input("Digite aqui o preço (R$) do exame: "))
                    hemograma_exame.necessita_jejum = input("Digite aqui se há necessidade de jejum: ").strip().capitalize()
                    lista_de_exames.append(hemograma_exame)
                    hemograma_exame.exibir_dados()
                elif definicao_exame == "Glicemia":
                    glicemia_exame = Glicemia()
                    glicemia_exame.codigo = input("Digite aqui o código do exame: ")
                    glicemia_exame.nome = input("Digite aqui o nome do exame: ")
                    glicemia_exame.preco = float(input("Digite aqui o preço (R$) do exame: "))
                    glicemia_exame.necessita_jejum = input("Digite aqui se há necessidade de jejum: ").strip().capitalize()
                    lista_de_exames.append(glicemia_exame)
                    glicemia_exame.exibir_dados()
                elif definicao_exame == "Colesterol":
                    colesterol_exame = Colesterol()
                    colesterol_exame.codigo = input("Digite aqui o código do exame: ")
                    colesterol_exame.nome = input("Digite aqui o nome do exame: ")
                    colesterol_exame.preco = float(input("Digite aqui o preço (R$) do exame: "))
                    colesterol_exame.necessita_jejum = input("Digite aqui se há necessidade de jejum: ").strip().capitalize()
                    lista_de_exames.append(colesterol_exame)
                    colesterol_exame.exibir_dados()
                else:
                    print("Opção inválida! Tente novamente")
                    continue
            elif decisao_menu_interno == 3:
                print("O processo foi concluido com sucesso!")
                break
    elif opcao_inicial == 3:
        mostrar_lista = Fila()
        if len(mostrar_lista) <= 0:
            print("Não há pacientes cadastrados")
            continue
        elif len(mostrar_lista) >= 1:
            print(mostrar_lista.exibir_resumo())
    
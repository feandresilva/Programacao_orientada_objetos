#13 - Modifique a classe Contato para incluir um método chamado editar, 
# que recebe dois parâmetros opcionais: 
# nome e telefone e redefine os atributos internos self.nome e self.telefone 
# de acordo com os parâmetros recebidos.
#14 - Adicione ao menu na função main a opção de Editar contato. Utilize o método
#buscar_contato da agenda para encontrar um contato, caso o contato exista na agenda, 
# permita que o usuário digite um novo nome/telefone e edite o contato usando o método 
# contato.editar(...).


class Contato:

    def __init__(self, nome: str, telefone: int):
        self.nome = nome
        self.telefone = telefone
    
    def __repr__(self):
        return f'{self.nome}, {self.telefone}'
    
    def __str__(self):
        return self.__repr__()
    
    def editar(self, nome=None, telefone=None):
        if nome:
            self.nome = nome
        if telefone:
            self.telefone = telefone
        

class Agenda:

    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, contato: Contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        return self.contatos
    
    def buscar_contato(self, nome):
        for contato in self.contatos:
            if nome == contato.nome:
                return contato

def main():
    minha_agenda = Agenda()

    while True:
        print("Menu:")
        print("1. Listar contatos")
        print("2. Adicionar contato")
        print("3. Buscar contato")
        print("4. Editar contato")
        print("5. Sair")
        escolha_menu = int(input("Digite o número da opção desejada: "))
        if escolha_menu == 1 and len(minha_agenda.listar_contatos()) > 0:
            print(f"Esta é a lista de contatos: {minha_agenda.listar_contatos()}")
        elif escolha_menu == 1 and len(minha_agenda.listar_contatos()) < 1:
            print("Ainda não há contatos cadastrados.")
        elif escolha_menu == 2:
            nome_inserir = input("Digite aqui o nome do contato: ").strip().capitalize()
            try:
                numero_inserir = int(input("Digite aqui o número do contato: "))
            except ValueError:
                print("Opção inválida! Por favor, tente novamente")
                continue
            contato_criado = Contato(nome_inserir, numero_inserir)
            minha_agenda.adicionar_contato(contato_criado)
            print("Contato criado com sucesso!")
        elif escolha_menu == 3 and len(minha_agenda.listar_contatos()) > 0:
            nome_buscar = input("Digite aqui o nome que deseja buscar: ").strip().capitalize()
            print(f"O resultado da sua pesquisa foi: {minha_agenda.buscar_contato(nome_buscar)}")
        elif escolha_menu == 3 and len(minha_agenda.listar_contatos()) < 1:
            print("Ainda não há contatos cadastrados!")
        elif escolha_menu == 4 and len(minha_agenda.listar_contatos()) > 0:
            nome_buscar = input("Digite aqui o nome que deseja buscar: ").strip().capitalize()
            nome_para_editar = minha_agenda.buscar_contato(nome_buscar)
            if nome_para_editar != None:                
                print(f"O resultado da sua pesquisa foi: {nome_para_editar}")
                editar_nome = input("Digite aqui o novo nome: ").strip().capitalize()
                editar_numero = int(input("Digite aqui o novo número: "))
                nome_para_editar.editar(editar_nome, editar_numero)
                print(minha_agenda.listar_contatos())            
                print(f'Alterações feitas com sucesso!')
            else:
                print("Esse usuário não existe! Tente novamente.")
                continue
        elif escolha_menu == 4 and len(minha_agenda.listar_contatos()) < 1:
            print("Ainda não há contatos cadastrados!")            
        elif escolha_menu == 5:
            print("Programa encerrado com sucesso!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue
main()
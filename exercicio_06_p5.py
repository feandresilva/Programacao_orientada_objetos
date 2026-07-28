#17 - Adicione à agenda um método "salvar" que armazena em um arquivo o dump da agenda. 
# Utilize a biblioteca pickle (Veja documentação: <https://docs.python.org/3/library/pickle.html>)

import pickle

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
            
    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato is not None:
            self.contatos.remove(contato)
        return contato
    
    def salvar (self):
        with open('contatos.pickle', 'wb') as f:
            pickle.dump(self.contatos, f, pickle.HIGHEST_PROTOCOL)

    def carregar_arquivo(self):
        with open('contatos.pickle', 'rb') as f:
            self.contatos = pickle.load(f)

def main():
    minha_agenda = Agenda()

    while True:
        print("Menu:")
        print("1. Listar contatos")
        print("2. Adicionar contato")
        print("3. Buscar contato")
        print("4. Editar contato")
        print("5. Remover contato")
        print("6. Salvar")
        print("7. Carregar arquivo")
        print("8. Sair")
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
        elif escolha_menu == 5 and len(minha_agenda.listar_contatos()) > 0:
            nome_para_remover = input("Digite aqui o nome que deseja buscar: ").strip().capitalize()
            contato_removido = minha_agenda.remover_contato(nome_para_remover)
            if contato_removido:
                print(f'O contato {contato_removido} foi removido com sucessso!')
            else:
                print("Contato não existente.")
                continue
        elif escolha_menu == 6:
            minha_agenda.salvar()
            print("Seu arquivo foi salvo com sucesso!")
        elif escolha_menu == 7:
            minha_agenda.carregar_arquivo()
            print("Seu arquivo foi carregado com sucesso!")
        elif escolha_menu == 8:
            print("Programa encerrado com sucesso!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue
main()
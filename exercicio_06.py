# 1 - Crie uma classe chamada `Contato` que possui os atributos: nome e telefone. 
# Defina esses atributos no método construtor `__init__`.

# 2 - Crie uma classe chamada `Agenda`. Essa classe servirá para armazenar contatos, 
# e terá um atributo chamado `contatos`, que deve ser inicializado como uma lista vazia.

# 3 - A classe Agenda também deve ter um método chamado `adicionar_contato`, 
# para incluir novos contatos, que recebe um objeto da classe Contato e 
# adiciona-o ao final da lista de contatos.

# 4 - Adicione o método `__repr__` à classe `Contato` que retorna a representação do contato. 
# Exemplo: "{nome},{telefone}"

# 5 - Adicione o método `__str__` à classe `Contato` que retorna `self.__repr__()`

# 6 - Adicione o método `listar_contatos` à classe `Agenda` que retorna a lista de contatos da agenda.

# 7 - Faça uma função `main` que: 
# - Cria uma agenda vazia com o construtor `Agenda()`;
# - Cria um novo contato, com nome e telefone informados pelo usuário;
# - Insere o novo contato na agenda, utilizando o método `adicionar_contato`
# - Por fim, exibe a agenda com o método `listar_contatos`.

# 8 - Chame a função `main` e teste o código do programa completo. 

# 9 - Altere a função main para inserir 3 novos contatos ao invés de apenas 1. Teste novamente o programa.

# 10 - Altere a função main para funcionar com um menu, com as seguintes opções:
# Listar contatos.
# Adicionar contato.
# Sair.

class Contato:

    def __init__(self, nome: str, telefone: int):
        self.nome = nome
        self.telefone = telefone
    
    def __repr__(self):
        return f'{self.nome}, {self.telefone}'
    
    def __str__(self):
        return self.__repr__()

class Agenda:

    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, contato: Contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        return self.contatos

def main():
    minha_agenda = Agenda()
    novo_contato = 0

    while novo_contato <= 2:
        nome_inserir = input("Digite aqui o nome do contato: ").strip().capitalize()
        try:
            numero_inserir = int(input("Digite o número de telefone do contato: "))
        except ValueError:
            print("Opção inválida! Insira números!")
            continue
        contato_criado = Contato(nome_inserir, numero_inserir)
        minha_agenda.adicionar_contato(contato_criado)
        novo_contato += 1
    print(minha_agenda.listar_contatos())

main()

#8 -Chame a função `main` e teste o código do programa completo. 

# 9 - Altere a função main para inserir 3 novos contatos ao invés de apenas 1. Teste novamente o programa.
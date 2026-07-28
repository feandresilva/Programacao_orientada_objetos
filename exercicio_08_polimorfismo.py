# 1 - Crie uma classe chamada DataFrame.

# 2 - A classe deverá possuir os atributos:
# columns, que armazena uma lista com os nomes das colunas;
# values, que armazena uma lista com os dados do DataFrame.

# 3 - Defina esses atributos no método construtor __init__.

# O atributo columns deverá ser recebido como parâmetro, 
# enquanto o atributo values deverá ser inicializado como uma lista vazia.

# Exemplo:

# df = DataFrame(["Nome", "Idade", "Cidade"])

# 4 - Adicione à classe DataFrame um método chamado append.

# Esse método deverá receber uma tupla contendo os valores de uma nova linha 
# e adicioná-la ao final da lista values.

# Exemplo:

# df.append(("Alice", 20, "Curitiba"))
# df.append(("Bruno", 25, "São Paulo"))

# 5 - Adicione à classe DataFrame o método __str__.

# Esse método deverá retornar uma string contendo:

# os nomes das colunas;
# todas as linhas armazenadas no atributo values.

# Cada linha deverá ser exibida separadamente.

# 6 - Faça um programa que:

# crie um objeto da classe DataFrame;
# defina pelo menos três colunas;
# adicione pelo menos três linhas utilizando o método append;
# exiba o DataFrame utilizando print(df).

# Exemplo de utilização:

# df = DataFrame(["Nome", "Idade", "Cidade"])

# df.append(("Alice", 20, "Curitiba"))
# df.append(("Bruno", 25, "São Paulo"))
# df.append(("Carla", 19, "Recife"))

# print(df)

class DataFrame():
    columns: list
    values: list

    def __init__(self, columns):
        self.columns = columns
        self.values = []

    def append(self, novos_valores):
        self.values.append(novos_valores)

    def __str__(self):
        return '\n'.join(map(str, [self.columns, *self.values]))



df = DataFrame(["Nome", "Idade", "Cidade"])
df.append(("Carlos", 25, "Campinas"))
df.append(("Alice", 20, "Curitiba"))
df.append(("Bruno", 25, "São Paulo"))
df.append(("Carla", 19, "Recife"))
print(df)
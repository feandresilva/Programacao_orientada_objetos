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

# 7 - Modifique a classe DataFrame para incluir o método especial __getitem__.

# Esse método deverá receber como parâmetro o nome de uma coluna.

# O método deverá procurar a posição da coluna dentro do atributo columns 
# e retornar uma lista contendo todos os valores dessa coluna.

# Exemplo 1:
# print(df["Nome"])

# Resultado Esperado:
# ["Alice", "Bruno", "Carla"]


# Exemplo 2:
# print(df["idade"])

# Resultado Esperado:
# [20, 25, 19]

# 8 - Adicione à classe DataFrame um método chamado to_csv.

# Esse método deverá receber como parâmetro o nome do arquivo 
# e salvar os dados do DataFrame em um arquivo CSV.

# A primeira linha do arquivo deverá conter os nomes das colunas, 
# armazenados no atributo columns.

# As linhas seguintes deverão conter os dados armazenados no atributo values.

# Exemplo:

# df.to_csv("produtos.csv")

# Conteúdo esperado do arquivo:

# Produto,Preço,Quantidade
# Camiseta,50.0,2
# Calça,120.0,3
# Tênis,250.0,1

import csv

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

    def __getitem__(self, coluna):
        if coluna not in self.columns:
            raise KeyError
        index = self.columns.index(coluna)
        return [linha[index] for linha in self.values]

    def to_csv(self, nome_arquivo):
        with open("nome_arquivo.csv", "w", newline= '', encoding='utf-8') as nome_arquivo:
            writer = csv.writer(nome_arquivo)
            writer.writerow(nome_arquivo)



df = DataFrame(["Nome", "Idade", "Cidade"])
df.append(("Carlos", 25, "Campinas"))
df.append(("Alice", 20, "Curitiba"))
df.append(("Bruno", 25, "São Paulo"))
df.append(("Carla", 19, "Recife"))
informacoes_pessoais = df
df.to_csv(informacoes_pessoais)
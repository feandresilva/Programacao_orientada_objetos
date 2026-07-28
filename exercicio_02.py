# Crie uma classe chamada "Produto" com os atributos:
# Código de barras,
# Nome, 
# Preço,
# Data de validade.

# Faça um programa que peça os dados de um produto para o usuário, 
# e crie um objeto com os atributos preenchidos, então mostre o objeto criado e seus atributos.

class Produto:
    codigo_barras: int
    nome: str
    preco: float
    data_validade: str

produto_1 = Produto()
produto_1.nome = input("Digite aqui o nome do produto: ")
produto_1.codigo_barras = int(input("Digite aqui o código de barras do produto: "))
produto_1.preco = float(input("Digite aqui o valor do preço: "))
produto_1.data_validade = input("Digite aqui a data de validade do produto: ")

print(f'O nome do produto é {produto_1.nome}, possui o código de barras {produto_1.codigo_barras}, preço no valor de R${produto_1.preco} e data de validade {produto_1.data_validade}')
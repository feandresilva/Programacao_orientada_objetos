#Crie uma classe chamada "EventoAleatorio".

#Ela deverá possuir o atributo:

#- possibilidades, que armazena uma lista de resultados possíveis.

#Adicione o método sortear, que deverá escolher e retornar aleatoriamente um elemento da lista 
# possibilidades.
#(utilize random.choice)

# Crie uma classe chamada "Moeda" que herda de "EventoAleatorio".
# Exemplo:

# class Moeda(EventoAleatorio):
#     ...

# A classe "Moeda" deverá definir o atributo possibilidades com os valores:

# ["Cara", "Coroa"]

# A classe "Moeda" não deverá criar um novo método sortear.

# Crie uma classe chamada "Dado" que herda de "EventoAleatorio".

# A classe "Dado" deverá definir o atributo possibilidades com os valores:

# [1, 2, 3, 4, 5, 6]

# A classe "Dado" não deverá criar um novo método sortear.

# Escreva uma função chamada "simular" que recebe como parâmetros:
# - evento (uma classe que herda de EventoAleatorio)
# - n (numero de repetições)

# Implemente na função a simulação de n repetições do evento, chamando o método sortear. 
# Mostre as informações na tela com print.

# Faça um programa que o usuário escolhe o evento (dentre Dado ou Moeda) e o número de repetições.
# O programa deve utilizar a função "simular" para executar a simulação de n repetições
#  do evento escolhido.


# Crie as seguintes classes, todas herdando de "EventoAleatorio":

# "Dado4";
# "Dado8";
# "Dado10";
# "Dado12";
# "Dado20".

# Cada classe deverá definir o atributo possibilidades de acordo com a quantidade de lados do dado.

# Por exemplo, a classe "Dado4" deverá possuir:

# [1, 2, 3, 4]

# A classe "Dado20" deverá possuir os números de 1 até 20.

# As classes filhas não deverão criar um novo método sortear.

# Permita que o usuário escolha dentre essas opções para a simulação.

# Crie uma classe chamada "Baralho" que herda de "EventoAleatorio".

# No método _init_, crie duas listas:

# valores = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

# naipes = ["Copas", "Ouros", "Espadas", "Paus"]

# Utilize essas listas para preencher o atributo self.possibilidades com todas as 52 combinações possíveis
# de valores e naipes.

# Exemplos de cartas:

# "Ás de Copas"
# "10 de Espadas"
# "Rei de Paus"

# A classe "Baralho" não deverá criar um novo método sortear.

import random

class EventoAleatorio():
    possibilidades: list

    def sortear(self):
        return random.choice(self.possibilidades)

class Moeda(EventoAleatorio):
    possibilidades = ["Cara", "Coroa"]

class Dado(EventoAleatorio):
    possibilidades = [1, 2, 3, 4, 5, 6]

class Dado4(EventoAleatorio):
    possibilidades = [1, 2, 3, 4]

class Dado8(EventoAleatorio):
    possibilidades = [1, 2, 3, 4, 5, 6, 7, 8]

class Dado10(EventoAleatorio):
    possibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Dado12(EventoAleatorio):
    possibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

class Dado20(EventoAleatorio):
    possibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

class Baralho(EventoAleatorio):
    def __init__(self):
        valores = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]
        naipes = ["Copas", "Ouros", "Espadas", "Paus"]
        self.possibilidades = [f'{valor} de {naipe}' for valor in valores for naipe in naipes]


def simular(evento, n):
    for i in range (n):
        print(f'Repetição {i+1}: {evento.sortear()}')



opcao_usuario = input("Qual opção você escolhe: Dado, Moeda ou Baralho? ").strip().capitalize()
repeticao_usuario = int(input("Digite o número de repetições desejada: "))
if opcao_usuario == "Dado":
    numero_lados = int(input("Quantos lados você deseja? 4, 6, 8, 10, 12 ou 20? "))
    if numero_lados == 4:
        simular(Dado4(), repeticao_usuario)
    elif numero_lados == 6:
        simular(Dado(), repeticao_usuario)
    elif numero_lados == 8:
        simular(Dado8(), repeticao_usuario)
    elif numero_lados == 10:
        simular(Dado10(), repeticao_usuario)
    elif numero_lados == 12:
        simular(Dado12(), repeticao_usuario)
    elif numero_lados == 20:
        simular(Dado20(), repeticao_usuario)
elif opcao_usuario == "Moeda":
    simular(Moeda(), repeticao_usuario)
elif opcao_usuario == "Baralho":
    simular(Baralho(), repeticao_usuario)
else:
    print("Opção inválida!")


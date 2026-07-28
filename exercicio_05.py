# Crie uma classe chamada "ContaBancaria".

# Ela deverá possuir os atributos:

# nome do titular;
# saldo.

# Adicione os métodos:

# depositar, que recebe um valor e adiciona ao saldo;

# sacar, que recebe um valor e subtrai do saldo, 
# desde que exista saldo suficiente;

# exibir_saldo, que mostra o saldo atual.

# Faça um programa que crie uma conta 
# e permita que o usuário escolha entre depositar, sacar, 
# consultar o saldo ou encerrar o programa.

import random

class ContaBancaria:
    nome_titular: str
    saldo: float

    def __init__(self):
        self.saldo = 0
        self.id = random.randint(1000, 10000)

    def __str__(self):
        return f"Conta número: {self.id}"

    def depositar(self, x):
        if x > 0:
            self.saldo += x
        else:
            print("Operação inválida.")
    
    def sacar(self, x):
        if self.saldo > x and x > 0:
            self.saldo -= x
        else:
            print("Operação não realizada. Saldo insuficiente")

    def exibir_saldo(self):
        return self.saldo

conta_01 = ContaBancaria()
while True:
    pergunta_inicial = input("O que deseja fazer? ").strip().capitalize()
    if pergunta_inicial == "Depositar":
        try:
            quantia_depositada = float(input("Digite a quantidade que deseja depositar: "))
        except ValueError:
            print("Opção inválida! Por favor, digite um número!")
            continue
        conta_01.depositar(quantia_depositada)
    elif pergunta_inicial == "Sacar":
        try:
            quantia_sacada = float(input("Digite a quantidade que deseja sacar: "))
        except ValueError:
            print("Opção inválida! Por favor, digite um número!")
            continue
        conta_01.sacar(quantia_sacada)
    elif pergunta_inicial == "Consultar":
        saldo_atual = conta_01.exibir_saldo()
        print(f'{conta_01}')
        print(f'Seu saldo atual é de R${saldo_atual}')
    elif pergunta_inicial == "Encerrar":
        print("Programa encerrado com sucesso!")
        break
    else:
        print("Opção inválida! Por favor, tente novamente.")
        continue
    


    



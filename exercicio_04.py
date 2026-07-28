# Crie uma classe "Calculadora".
# Ela deverá possuir o atributo "x", 
# que representa o número atual armazenado na memória da calculadora. 
# Inicialmente ele é zero.

# Faça os métodos:
# soma -> recebe como parâmetro um número y 
# e adiciona-o ao atributo self.x

# sub -> recebe como parâmetro um número y
# e subtrai-o do atributo self.x

# mult -> recebe como parâmetro um número y e redefine o self.x 
# como o produto do x pelo y

# div -> recebe como parâmetro um número y e redefine o self.x 
#como o produto do x pelo y

# Faça então um programa que instancie uma calculadora
# e execute um loop indefinido (while true) 
# em que o usuário insere uma operação e um número, 
# e então efetuar a operação utilizando os métodos do objeto calculadora,
# e exibir o resultado na tela. 
# O programa se encerra quando o usuário digitar "sair".

class Calculadora:
    x: float

    def soma(self, y):
        self.x += y
        return self.x

    def sub(self,y):
        self.x -= y
        return self.x

    def mult(self, y):
        self.x *= y
        return self.x

    def div(self, y):
        self.x /= y
        return self.x

calculadora_1 = Calculadora()
calculadora_1.x = 0
while True:
    operacao = input("Digite aqui qual operação você deseja: ").strip().capitalize()
    try:
        numero_digitado = float(input("Digite aqui um número: "))
    except ValueError:
        print("Por favor, digite um número!")
        continue
    if operacao == "Adicao":
        resultado = calculadora_1.soma(numero_digitado)
    elif operacao == "Subtracao":
        resultado = calculadora_1.sub(numero_digitado)
    elif operacao == "Multiplicacao":
        resultado = calculadora_1.mult(numero_digitado)
    elif operacao == "Divisao":
        resultado = calculadora_1.div(numero_digitado)
    else:
        print("Operação inválida!")
        continue
    print(f'O resultado é {resultado}')
    pergunta_usuario = input("Deseja continuar ou sair? ").strip().capitalize()
    if pergunta_usuario == "Sair":
        print("Obrigado por usar nossa calculadora!")
        break
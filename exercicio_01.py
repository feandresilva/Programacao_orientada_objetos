#Crie uma classe "Pessoa", que possui os atributos "nome" e "idade".
#Crie um objeto dessa classe, atribua a ela o nome "Alice" e a idade "20".
#Exiba os atributos desse objeto.

class Pessoa:
    nome: str
    idade: int

pessoa1 = Pessoa()
pessoa1.nome = "Alice"
pessoa1.idade = 20

print(f'O nome é {pessoa1.nome}, idade é {pessoa1.idade} anos.')

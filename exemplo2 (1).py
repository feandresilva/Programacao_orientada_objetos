
class Contato:
    nome: str
    telefone: int
    email: str


class Agenda:
    lista_contatos: list



### 


class Piloto:
    nome: str
    altura: float
    idade: int


class Carro:
    nome: str
    numero: int
    velocidade: float
    aceleracao: float

    def dar_partida(self):
        print(f"Iniciando carro {self.nome}")


class Motor:
    nome: str
    potencia: int


class Pneu:
    tipo: str
    durabilidade: int


carro1 = Carro()
carro1.nome = "fusca"
carro1.numero = 10


carro1.dar_partida()
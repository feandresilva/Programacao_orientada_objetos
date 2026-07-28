# Crie uma classe "Relogio"
# Ela possui o atributo "horas".
# Adicione o método "avancar" à classe Relogio, que deverá adicionar mais 1 hora ao relogio. 
# Mas garanta que ao avançar da hora 23, o relógio volte para 0 horas.

# Faça um programa que cria um objeto da classe Relogio e avança a hora 30 vezes com um loop for, 
# e utilizando o método "avancar".

import time

class Relogio:
    horas: int

    def avancar(self):
        self.horas += 1
        if self.horas > 23:
            self.horas = 0
relogio_1 = Relogio()
relogio_1.horas = 0
for i in range (30):
    relogio_1.avancar()
    print(relogio_1.horas)
    time.sleep(1)
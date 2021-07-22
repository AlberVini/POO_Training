from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, estado):
        self.nome = nome
        self.idade = idade
        self.estado = estado

    def ano_nascimento(self):
        ano_nasc = Pessoa.ano_atual - self.idade
        return f'{self.nome} nasceu no ano de {ano_nasc}'

    def info(self):
        return f'{self.nome} tem {self.idade} anos e mora no Estado de {self.estado}'

    # pode ser utilizado como um construtor, para por exemplo ajustar valores passados do usuário
    @classmethod
    def passagem_ano_nascimento(cls, nome, ano_nascimento, cidade):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade, cidade)

    @classmethod
    def ajuste_por_string(cls, pessoa_str):
        nome, idade, estado = pessoa_str.split('-')
        return cls(nome, int(idade), estado)

    # staticmethod é como uma função comum, portanto, pode ser usado de forma independente
    @staticmethod
    def gera_id():
        num = randint(1000, 1999)
        return num


# passagem direta por classe
p1 = Pessoa('Gustavo', 30, 'RJ')
print(p1.info())

# passagem por classmethod, adequando os valores passados por váriavel 
pessoa_string = 'João-21-SP'
p2 = Pessoa.ajuste_por_string(pessoa_string)
print(p2.info())

# passagem por classmethod, ajustando o valor do parametro idade passado como ano_nasc
p3 = Pessoa.passagem_ano_nascimento('Maria', 1987, 'PR')
print(p3.info())
print(p3.ano_nascimento())

p4 = Pessoa('Clara', 19, 'GO')
id = p4.gera_id()
print(f'{p4.info()} e tem o id = {id}')

print(Pessoa.gera_id())

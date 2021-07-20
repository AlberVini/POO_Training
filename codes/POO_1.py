from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, curso, comendo = False):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.comendo = comendo

    def __repr__(self):
        return f"{self.nome} tem {self.idade} anos e está cursando {self.curso}."

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} não pode comer {alimento}, porque já está comendo')
        else:
            print(f'{self.nome} está comendo {alimento}')
            self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} já não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def ano_nascimento(self):
        return self.ano_atual - self.idade
    

p1 = Pessoa('Luiz', 18, 'Sistemas da Informação')
print(p1) # chama o método __repr__
p1.comer('Maçã')
p1.parar_comer()
print(f'{p1.nome} nasceu no ano de {p1.ano_nascimento()}')

print('-' * 50)

p2 = Pessoa('Júlia', 26, 'Nutrição', True)
print(p2)
p2.comer('Chocolate')
p2.parar_comer()
print(f'{p2.nome} nasceu no ano de {p2.ano_nascimento()}')

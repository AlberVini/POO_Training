class Npc:
    def __init__(self, nome, time, ataque=100, defesa=100, vida=100, status = True):
        self.nome = nome
        self.time = time
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida
        self.status = status
        self.classe = self.__class__.__name__

    def info(self):
        print('-' * 25)
        print(f'Nome........: {self.nome}')
        print(f'Classe......: {self.classe}')
        print(f'Time........: {self.time}')
        print(f'Ataque......: {self.ataque}')
        print(f'Defesa......: {self.defesa}')
        print(f'Status......: {"Vivo" if self.status else "Morto"}')
        print(f'Vida........: {self.vida}')


class Soldado(Npc):
    def __init__(self, nome, time, status = True):
        self.vida = 300
        self.ataque = 300
        self.defesa = 300
        super().__init__(nome, time, self.ataque, self.defesa, self.vida, status = status)


class Atirador(Npc):
    def __init__(self, nome, time, status = True):
        self.vida = 200
        self.ataque = 400
        self.defesa = 200
        super().__init__(nome, time, self.ataque, self.defesa, self.vida, status=status)


class Tanque(Npc):
    def __init__(self, nome, time, status = True):
        self.vida = 400
        self.ataque = 200
        self.defesa = 400
        super().__init__(nome, time, self.ataque, self.defesa, self.vida, status=status)


npc = Npc('Joe', 0)
p1 = Soldado('Everton', 1)
p2 = Atirador('Saulo', 1)
p3 = Tanque('Pedro', 1)
p4 = Soldado('Claúdio', 2)
p5 = Atirador('Felipe', 2)
p6 = Tanque('Henrique', 2)

npc.info()
p1.info()
p2.info()
p3.info()
p4.info()
p5.info()
p6.info()

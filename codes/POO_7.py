class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.lista_enderecos = []

    def adicionar_endereco(self, cidade, estado):
        self.lista_enderecos.append(Enderecos(cidade, estado))

    def mostrar_enderecos(self):
        for endereco in self.lista_enderecos:
            print(self.nome, endereco.cidade, endereco.estado)

    # __del__ apaga os objetos criados a partir dessa classe, no final ou
    # quando a palavra del(obj) for acionada
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')
    

class Enderecos:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


p1 = Pessoa('Paulo')
p1.adicionar_endereco('Sâo Paulo', 'SP')
p1.adicionar_endereco('Campinas', 'SP')
p1.mostrar_enderecos()
del p1

p2 = Pessoa('Maria')
p2.adicionar_endereco('Rio de Janeiro', 'RJ')
p2.mostrar_enderecos()

p3 = Pessoa('Pedro')
p3.adicionar_endereco('Curitiba', 'PR')
p3.mostrar_enderecos()
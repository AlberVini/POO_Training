from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, ano_nasc, cidade):
        self.nome = nome
        self.ano_nasc = ano_nasc
        self.cidade = cidade
        self.lista_clientes = {'clientes': {}, 'idade': {}, 'cidade': {}}

    def criacao_dic(self):
        self.lista_clientes['clientes'] = self.nome
        self.lista_clientes['idade'] = self.obter_idade()
        self.lista_clientes['cidade'] = self.cidade

    def infos(self):
        for key, item in self.lista_clientes.items():
            print(self.lista_clientes)
            print(key, item)

    @classmethod
    def por_ano_nascimento(cls, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return idade

    def obter_idade(self):
        idade = self.por_ano_nascimento(self.ano_nasc)
        return idade


p1 = Pessoa('Vinicius', 1997, 'SP')
p1.criacao_dic()
p2 = Pessoa('Júlia', 1980, 'RJ')
p2.criacao_dic()
p2.infos()

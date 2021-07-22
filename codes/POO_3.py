import re

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        preco_desc = self.preco - (self.preco * (porcentagem / 100))
        return 'O {} com {}% de desconto custará R${:.2f}'.format(self.nome, porcentagem, preco_desc)

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor1 = re.sub(r'\w\$', '', valor)
            self._preco = float(valor1[0])
        else:
            self._preco = float(valor)


prod = Produto('Camiseta', 30)
print(prod.desconto(10))

prod1 = Produto('Luva', 'R$8')
print(prod1.desconto(5))
class CarrinhoCompras:
    def __init__(self):
        self.lista_prod = []

    def inserir_prod(self, produto):
        self.lista_prod.append(produto)

    def exibir_produtos(self):
        for prod in self.lista_prod:
            print(f"{prod.nome} R$ {prod.valor}")

    def soma_prod(self):
        tot = 0
        for unidade in self.lista_prod:
            tot += unidade.valor
        return f"Total de R$ {tot}"


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoCompras()
p1 = Produto('Camisa', 30)
p2 = Produto('Tenis', 220)
p3 = Produto('Fone', 120)

carrinho.inserir_prod(p1)
carrinho.inserir_prod(p2)
carrinho.inserir_prod(p3)
carrinho.inserir_prod(p2)

carrinho.exibir_produtos()

print(carrinho.soma_prod())
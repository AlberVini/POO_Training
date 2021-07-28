"""
public, protected, private
(Sem _) public, pode ser livremente usado
_ protected, private(forma mais fraca), por boa pratica, uma variável com _ não deve ser acessada
__ private(forma mais forte), ainda mais restrição para não ser usada
"""


class BaseDados:

    def __init__(self):
        self.__dados = {}

    # Fazendo o nome ser visivel novamente
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = ({id: nome})
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for ind, nome in self.__dados['clientes'].items():
            print(ind, nome)
        return

    def deletar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDados()
bd.inserir_cliente(1, 'Vinicius')
bd.inserir_cliente(2, 'Pedro')
bd.inserir_cliente(3, 'Carla')
bd.lista_clientes()

# print(bd.dados)
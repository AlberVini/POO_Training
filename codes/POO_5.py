class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None


class Caneta:
    def __init__(self, marca):
        self.marca = marca
        self.escrevendo = False

    def escrever(self, nome=None):
        if nome == None:
            self.escrevendo = True
            print(f"Caneta da marca {self.marca} está escrevendo.. ")
            return
        else:
            self.escrevendo = True
            print(f"{nome} está escrevendo com a caneta da marca {self.marca}")
            return

    def parar_escrever(self):
        if self.escrevendo:
            self.escrevendo = False
            print("Parando de escrever...")
            return
        else:
            print('Caneta já não está escrevendo')


class Maquina:
    @staticmethod
    def escrever():
        print('Escrevendo..')


escritor = Escritor('José')
caneta = Caneta('Bic')
maquina = Maquina()

caneta.escrever()
caneta.parar_escrever()

# atributos de classe X podem receber um objeto Y, sendo assim, 
# o atributo pode obter os métodos da classe do objeto Y
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever(escritor.nome)

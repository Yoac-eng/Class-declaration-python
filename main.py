
#Abstração
import this


class Pessoa:
    def __init__(self, nome, cpf, rg, data_nasc, sexo):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.data_nasc = data_nasc
        self.sexo = sexo

        def falar(self):
            print('Bom dia, gostaria de obter informações sobre esse carro.')

#Abstração e hierarquia
class Client(Pessoa):
    def _init_(self, comprov_res):
        self.comprov_res = comprov_res

        def comprarCarro(self, modelo):
            print('Esse carro.')
        #Polimorfismo
        def falar(self):
            print('Tudo bem então, irei comprar esse carro mesmo.')

#Abstração 
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

        def ligar(self):
            print("ligando carro...")
        def locomover(self):
            print("vrum vrum")
    
class Venda:
    #Encapsulamento
    def __init__(self, vendedor, produto, comprador, data_venda, valor_venda):
        self.__vendedor = vendedor
        self.__produto = produto
        self.__comprador = comprador
        self.data_venda = data_venda
        self.valor_venda = valor_venda

        def vender(self):
            print("Vendendo...")
        def cancelarVenda(self):
            print("Cancelando venda...")

        def getVendedor(self):
            return self.__vendedor

        def setVendedor(vendedor):
            self.__vendedor = vendedor

        def getProduto(self):
            return self.__produto

        def setProduto(produto):
            self.__produto = produto

        def getComprador(self):
            return self.__comprador

        def setComprador(comprador):
            self.__comprador = comprador
        

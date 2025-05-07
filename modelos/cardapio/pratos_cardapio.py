from modelos.cardapio.itens_cardapio import ItemCardapio

class Pratos(ItemCardapio):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.descricao = description

    def desconto(self):
        self._preco -= (self._preco*0.1)
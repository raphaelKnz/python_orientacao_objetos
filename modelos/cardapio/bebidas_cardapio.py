from modelos.cardapio.itens_cardapio import ItemCardapio

class Bebidas(ItemCardapio):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.tamanho = size
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, name, price):
        self._nome = name
        self._preco = price
    
    def desconto(self):
            pass
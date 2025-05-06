from modelos.avaliacao import Avaliacao
from modelos.cardapio.itens_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, name, category):
        self._nome = name
        self._categoria = category
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Nota'.ljust(20)} {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.activo.ljust(20)}')
        
    def alternar_status(self):
        self._status = not self._status

    @property
    def activo(self):
        return 'Ativado' if self._status else 'Desativado'
    
    def receber_avaliacoes(self, client, grade):
        if 0>grade or grade>5:
            print(f'nota do cliente {client} fora do permitido')
            return
        avaliacao = Avaliacao(client, grade)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = 0
        for i in self._avaliacao:
            soma += i._nota
        media = soma/len(self._avaliacao)
        return media

    def adicionar_item_cardapio(self, item):
        if (isinstance(item, ItemCardapio)):
            self._cardapio.append(item)

    def listar_cardapio(self):
        print(f'Cardápio do {self._nome} restaurants')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr (item, 'descricao'):
                msg_prato = f'{i}. Nome: {item._nome.ljust(15)} | Preço: R$ {str(item._preco).ljust(15)} | Descrição: {item.descricao.ljust(15)}'
                print(msg_prato)
            elif hasattr (item, 'tamanho'):
                msg_bebida = f'{i}. Nome: {item._nome.ljust(15)} | Preço: R$ {str(item._preco).ljust(15)} | Tamanho: {item.tamanho.ljust(15)}'
                print(msg_bebida)

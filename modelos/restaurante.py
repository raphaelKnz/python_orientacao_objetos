class Restaurante:
    restaurantes = []
    def __init__(self, name, category):
        self._nome = name
        self._categoria = category
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.activo.ljust(20)}')
        
    def alternar_status(self):
        self._status = not self._status

    @property
    def activo(self):
        return 'Ativado' if self._status else 'Desativado'
    
    def receber_avaliacoes(self, client, nota):
        self._avaliacao = nota
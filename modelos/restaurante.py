from modelos.avaliacao import Avaliacao

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
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Nota'.ljust(20)} {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.activo.ljust(20)}')
        
    def alternar_status(self):
        self._status = not self._status

    @property
    def activo(self):
        return 'Ativado' if self._status else 'Desativado'
    
    def receber_avaliacoes(self):
        quantidade_avaliadores = 0
        try:
            quantidade_avaliadores = int(input('quantas pessoas querem avaliar o restaurante: '))
        except ValueError:
            print('Digite um numero válido')
            return
        for i in range(quantidade_avaliadores):
            client = str(input('entre com seu nome: '))
            while True:
                try:
                    grade = float(input('entre com sua avaliacao de 0 a 5 estrelas: '))
                    if 0<grade and grade<5:
                        break
                    else:
                        print(f'nota do cliente {client} fora do permitido')
                except ValueError:
                    print('Digite um numero válido')
            
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

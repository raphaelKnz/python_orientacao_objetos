from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas_cardapio import Bebidas
from modelos.cardapio.pratos_cardapio import Pratos

restaurante_pizza = Restaurante('Pizza Planet', 'Pizzaria')
restaurante_japones =  Restaurante('Orientas', 'Japonesa')
restaurante_pizza.receber_avaliacoes('jao',8)
restaurante_pizza.receber_avaliacoes('jul', 4)
restaurante_pizza.receber_avaliacoes('das', 5)
restaurante_japones.receber_avaliacoes('op', 7)
restaurante_japones.receber_avaliacoes('op', 5)
restaurante_japones.receber_avaliacoes('op', 3)
pao_manha=Pratos('Pão Francês', 3.5, 'O melhor')
suco_de_uva = Bebidas('Suco de Uva', 7, 'Médio')
pefe= Pratos('PF', 20, 'Do dia')

def main():
    restaurante_japones.alternar_status()
    restaurante_japones.adicionar_item_cardapio(pao_manha)
    restaurante_japones.adicionar_item_cardapio(suco_de_uva)
    restaurante_pizza.adicionar_item_cardapio(pefe)
    pefe.desconto()
    suco_de_uva.desconto()
    print('\n')
    Restaurante.listar_restaurantes()
    print('\n')
    Restaurante.listar_cardapio(restaurante_japones)
    Restaurante.listar_cardapio(restaurante_pizza)
    print('\n')


if __name__ == '__main__':
    main()
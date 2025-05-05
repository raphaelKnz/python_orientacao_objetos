from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('Pizza Planet', 'Pizzaria')
restaurante_japones =  Restaurante('Orientas', 'Japonesa')
restaurante_japones.alternar_status()
restaurante_pizza.receber_avaliacoes('jao',8)
restaurante_pizza.receber_avaliacoes('jul', 4)
restaurante_pizza.receber_avaliacoes('das', 5)
restaurante_japones.receber_avaliacoes('op', 7)
restaurante_japones.receber_avaliacoes('op', 5)
restaurante_japones.receber_avaliacoes('op', 3)

Restaurante.listar_restaurantes()
from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('Pizza Planet', 'Pizzaria')
restaurante_japones =  Restaurante('Orientas', 'Japonesa')
restaurante_japones.alternar_status()
restaurante_pizza.receber_avaliacoes()
restaurante_japones.receber_avaliacoes()

Restaurante.listar_restaurantes()
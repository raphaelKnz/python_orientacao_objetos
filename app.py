from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('Pizza Planet', 'Pizzaria')
restaurante_japones =  Restaurante('Orientas', 'Japonesa')
restaurante_japones.alternar_status()

Restaurante.listar_restaurantes()
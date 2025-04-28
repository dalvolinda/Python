from modelos.restaurante import Restaurante

restaurante_japex = Restaurante('Japex', 'japonesa')
restaurante_japex.receber_avaliacao('Dalvolinda', 5)
restaurante_japex.receber_avaliacao('Maria', 0)
restaurante_japex.receber_avaliacao('Jose', 4)

restaurante_central = Restaurante('Central', 'buffet')
restaurante_central.receber_avaliacao('Paulo', 5)
restaurante_central.receber_avaliacao('João', 3)
restaurante_central.receber_avaliacao('Ana', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
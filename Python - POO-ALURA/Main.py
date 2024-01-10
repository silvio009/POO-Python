
from Modelos.Restaurante import Restaurante
from Modelos.cardapio.prato import Prato
from Modelos.cardapio.bebida import Bebida


restaurante1 = Restaurante('Restaurante JK' , 'Hamburguer')

prato_novo = Prato("Fritas com queijo",12," Batata com cheddar e bacon")
prato_novo.aplicar_desconto()
bebida_nova = Bebida("Suco de uva",8,'Médio')
bebida_nova.aplicar_desconto()

restaurante1.add_no_cardapio(bebida_nova)
restaurante1.add_no_cardapio(prato_novo)

def main():
   restaurante1.exibir_cardapio
   

# tornando o arquivo main
if __name__ == '__main__':
    main()
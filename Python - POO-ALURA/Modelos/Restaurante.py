from Modelos.Avaliacao import Avaliacao
from Modelos.cardapio.item_cardapio import ItemCardapio


#Classe para Restaurante
class Restaurante:
    restaurantes= []

    # construtor(parametros || instancia)
    # colocar o _ antes do atributo deixa ele "privado",sem poder ser alterado pelo usuário
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []

        Restaurante.restaurantes.append(self)

    # função para mostrar os valores do objeto com __str__
    def __str__(self):
        return f'{self._nome} || {self._categoria} || {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurente:'.ljust(25)}||{'Categoria:'.ljust(25)}||{'Avaliação:'.ljust(25)}|| {'Status:'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)}||{restaurante._categoria.ljust(25)}||{str(restaurante.media_avaliacaoes).ljust(25)}||{restaurante.ativo}')
    
    # modificar como o atributo vai ser lido 
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacaoes(self):
        if not self._avaliacao:
            return 0
        somaDasNotas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidadeNotas = len(self._avaliacao)

        media = round(somaDasNotas / quantidadeNotas,1) 
        return media

    def add_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)


    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante{self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            # hasattr == se tiver o atributo
            if hasattr(item,'descricao'):
               msg_prato = f'{i}. Nome:{item._nome} | Preço R${item._preco} | Descrição:{item.descricao}'
               print(msg_prato)
            else:
             msg_bebida =  f'{i}. Nome:{item._nome} | Preço R${item._preco} | Tamanho:{item.tamanho}'
             print(msg_bebida)
           









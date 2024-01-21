#import json (não preciso mais disso)

from classes.AbstractCrud import AbstractCrud          #*********Vou importar essa classe****

class Produto(AbstractCrud):                    # **** herdo a classe /// passo a ter todos os métodos

    arquivo = 'db/produtos.json' 
    
    def __init__(self, codigo, nome , quantidade = 0, valor = 0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
                                            # não pode fazer no abstractCrud. é uma verificação especifica do produto
                                            # Vamos utilizar o POLIMORFISMO
                                     #  Sobre escrever o método inserir aplicando uma regra. Não chama o do pai. sempre do filho


    def inserir(self):                 
        lista = self.consultar()
        produtoDuplicado = filter(lambda p: p['codigo'] == self.codigo, lista)

        #print(list(produtoDuplicado))    ///// só para listar

        if len(list(produtoDuplicado)):
            print()
            print('Já existe um produto com esse código')
        else:
            super().inserir()




   # *** TUDO ABAIXO FOI PARA O ARQUIVO INDEX.PY ***     
   # produto0 = Produto( '001', 'Samsung', '20', '5000')

   # produto1 = Produto('002', 'LG', '30', '2000')

    #produto2 = Produto('003', 'Nokia', '40')#

    #print(produto0.__dict__)
    #print(produto1.__dict__)
    #print(produto2.__dict__)

    # ******** TUDO ABAIXO FOI PARA O ARQUIVO ABSTRACTCRUD ************ 

    #def detalhar(self):
     #   return self.__dict__
    
    #def inserir(self):
        
     #   try:
      #      with open('db/produtos.json') as file:
       #         lista = json.load(file)

    #    except Exception:
     #       lista = []
        
      #  lista.append(self.detalhar())

       # with open('db/produtos.json', 'w') as file:
        #    json.dump(lista, file, indent=4)

     #   print('Registro cadastrado com sucesso')

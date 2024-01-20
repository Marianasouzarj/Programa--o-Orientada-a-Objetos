#import json (não preciso mais disso)

from classes.AbstractCrud import AbstractCrud          #*********Vou importar essa classe****

class Produto(AbstractCrud):                    # **** herdo a classe /// passo a ter todos os métodos
    
    def __init__(self, codigo, nome , quantidade = 0, valor = 0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor


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

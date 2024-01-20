import json
from abc import ABC

class AbstractCrud(ABC):

    def detalhar(self):
        return self.__dict__
    
    def inserir(self):
        lista = self.consultar()
        lista.append(self.detalhar())
        self.__gravarArquivo(lista)                   # ------ Método privado (Tem 2 __)

    def alterar(self, item):
        lista = self.consultar()
        lista[item] = self.detalhar()
        self.__gravarArquivo(lista)       # ----Dps q criado o metodo grava... essa linha substitui as 3 debaixo----
         
        #with open(self.arquivo, 'w') as file:
        #    json.dump(lista, file, indent=4)

        #print('Registro alterado com sucesso')

    def __gravarArquivo(self, lista):
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)

        print('Operação realizada com sucesso')

    @classmethod
    def excluir(cls, item):
        lista = cls.consultar()
        del lista[item]
         
        with open(cls.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)

        print('Operação realizada com sucesso')
         

    @classmethod
    def listarTodos(cls):
            lista = cls.consultar()

            for i, p in enumerate(lista):
                print(f"{i} - {p}")

    @classmethod
    def consultar(cls, item = None):
        try:
            with open(cls.arquivo) as file:      # ****** atributo de classe *******
                lista = json.load(file)

            return lista [item] if isinstance(item, int) else lista  # essa linha substitui as debaixo  
              
              #if isinstance(item, int):
              #      return lista [item]
             #     else:
             #       return lista 
         
        except Exception:
            return []
            



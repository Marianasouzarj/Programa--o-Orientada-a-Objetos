from classes.Produtoteste import Produto

def menu():
    print()
    print('1 - Listar Produtos')
    print('2 - Inserir Produtos')
    print('3 - Alterar Produtos')
    print('4 - Excluir Produtos')
    print('0 - Sair')
    print()


opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            print()
            print('************************************************************************************************')
            Produto.listarTodos()
            print('************************************************************************************************')

        case 2: 
            codigo = input('Digite o código: ')
            nome = input('Digite o nome: ')
            quantidade = input('Digite a quantidade: ')
            valor = input('Digite o valor: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()

        case 3:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja alterar? '))
            item = Produto.consultar(selecionado)
            print(selecionado)
            print(item)

            quantidade = int(input('Qual a nova quantidade? ')) 
            valor = int(input('Qual o novo valor? ')) 

            produto = Produto(item['codigo'], item['nome'], quantidade, valor)
            produto.alterar(selecionado)

        case 4:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja excluir? '))
            Produto.excluir(selecionado)


print()
print('Até a próxima!')
    



















#Produto.excluir(0) 


#item = 4
#itemAlterar = Produto.consultar(item)

#produto = Produto(itemAlterar['codigo'], itemAlterar['nome'], 300, 150) 
#produto.alterar(item)


#produto = Produto('123', 'tênis', 200, 80)

#produto.inserir()
#produto.listarTodos()

#categoria = Categoria('Eletrônico')
#print(categoria.detalhar())

#categoria = Categoria('eletrônico')
#categoria.inserir()
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista = []

while True:
    print('[i]nserir [a]pagar [l]istar')
    comando = input('escolha uma da alternativa: ')

    if comando == 'i':
        produto = input('fale o produto a inserir: ')
        lista.append(produto)

    elif comando == 'a':
        excluir= input('esolha o indice a ser excluido:')

        try:
            excluir = int(excluir)
            del lista[excluir]

        except IndexError:
            print("indice não existe na lista")

        except Exception:
            print('erro desconhecido')

        except TypeError:
            print('por favor escola um número inteiro')
    
    elif comando == 'l':
        
        if len(lista) == 0:
            print('nada para mostrar na lista')
        
        for indice, listar in enumerate(lista):
            print(indice, listar)
    
    else:
        print('escolha entre i, a e l.')

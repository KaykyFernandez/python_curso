"""
exercico
exiba os índices da lista
0 maria
1 helena
2 luiz
"""
lista = ['kayky', 'flavia', 'maria']
lista.append('joao')

i = range(len(lista))

for indice in i:
    print(indice, lista[indice], type(lista[indice]))
   
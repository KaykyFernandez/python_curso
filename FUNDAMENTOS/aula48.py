"""
lista em python
 tipo de list - Mutável
 suporta vários valores de qualquer tipo
 conhecimento reutilizáveis - indices e fatiamento
 métodos úteis:
   append = adiciona item no final
   insert = adiciona intem no indice escolhido
   pop = remove do final ou indice escolhido
   del = apaga um indice
   clear  = limpa a lista
   extend = estende a lista
   + = concatena listas
   Create Read Update Delete
   Criar,  ler,  alterar, apagar = lista[i] (CRUD)
 """

string = 'abcde' # 5 caracters (len)

#print(bool([])) #false
#print(lista, type(lista))
#         0    1     2                 3     4
#         -5   -4     -3               -2   -1
lista = [10, 20, 30, 40 ]

lista.append('lala')
lista.pop(0) #evitar isso em começo de lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()

#lista[-3] = 'maria'
print(lista, 'removido', ultimo_valor)
#del lista[2]
#print(lista[2])
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
print(lista[4])
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)